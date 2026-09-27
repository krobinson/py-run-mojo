import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import subprocess
    import tempfile
    import shutil
    import sys
    from pathlib import Path

    # 1. Fill in your template variables
    width, height, max_iter = 80, 40, 100
    # Mojo body is indented one level deeper than the cell code so marimo's
    # cell dedent can't strip the template's indentation.
    mojo_template = """def main():
        var width = {{width}}
        var height = {{height}}
        var max_iter = {{max_iter}}

        for py in range(height):
            var row = String("")
            for px in range(width):
                var x0 = (Float64(px) / Float64(width)) * 3.5 - 2.5
                var y0 = (Float64(py) / Float64(height)) * 2.0 - 1.0
                var x = 0.0
                var y = 0.0
                var i = 0
                while x * x + y * y <= 4.0 and i < max_iter:
                    var xt = x * x - y * y + x0
                    y = 2.0 * x * y + y0
                    x = xt
                    i += 1
                if i == max_iter:
                    row += "#"
                else:
                    row += "."
            print(row)
    """

    mojo_code = (
        mojo_template.replace("{{width}}", str(width))
        .replace("{{height}}", str(height))
        .replace("{{max_iter}}", str(max_iter))
    )

    # 2. Write to a temporary file and execute it
    with tempfile.NamedTemporaryFile(suffix=".mojo", mode="w", delete=False) as f:
        f.write(mojo_code)
        temp_file_path = f.name

    # 3. Run via Mojo CLI
    MOJO = shutil.which("mojo") or str(Path(sys.executable).parent / "mojo")
    result = subprocess.run([MOJO, temp_file_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)
    print("Mojo CLI output:")
    print(result.stdout)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(mo):
    dir(mo)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()

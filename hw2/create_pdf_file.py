from pdflatex import PDFLaTeX
from texutils_hw2 import image_to_tex, list_to_table

table_example = [[1, 2, 3], ["a", "b", "c"], [3.1, "python", 4]]
image_path = "artifacts/2.2/donald-duck-smiling.png"
document_template = r"""\documentclass{{article}}
\usepackage{{graphicx}}
\begin{{document}}{0}
{1}
\end{{document}}"""

if __name__ == "__main__":
    with open("artifacts/2.2/table_and_image.tex", "w") as f:
        formatted_tex_table = list_to_table(table_example)
        formatted_tex_image = image_to_tex(image_path)
        document = document_template.format(formatted_tex_table, formatted_tex_image)
        f.write(document)

    pdfl = PDFLaTeX.from_texfile("artifacts/2.2/table_and_image.tex")
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)

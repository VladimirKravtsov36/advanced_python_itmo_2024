from texutils_hw2.table import list_to_table

table_example = [[1, 2, 3], ["a", "b", "c"], [3.1, "python", 4]]
document_template = r"""\documentclass{{article}}
\begin{{document}}{0}
\end{{document}}"""

if __name__ == "__main__":
    with open("artifacts/2.1/table_example.tex", "w") as f:
        formatted_tex_table = list_to_table(table_example)
        document = document_template.format(formatted_tex_table)
        f.write(document)

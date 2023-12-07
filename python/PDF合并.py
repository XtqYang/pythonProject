from PyPDF2 import PdfMerger


def merge_pdfs(input_paths, output_path):
    merger = PdfMerger()

    for path in input_paths:
        merger.append(path)

    merger.write(output_path)
    merger.close()


# 示例用法
input_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
output_file = "merged.pdf"

merge_pdfs(input_files, output_file)

import re
import subprocess

def modify_latex_file(input_file, output_file, selected_components):
    with open(input_file, "r", encoding="utf-8") as f:
        tex_lines = f.readlines()

    filtered_lines = []
    include_section = False

    for line in tex_lines:
        section_match = re.match(r"\\section{(.+?)}", line)
        subsection_match = re.match(r"\\subsection{(.+?)}", line)

        if section_match:
            section_name = section_match.group(1)
            include_section = section_name in selected_components

        if subsection_match:
            subsection_name = subsection_match.group(1)
            include_section = subsection_name in selected_components

        if "\\begin{tabular" in line or "\\includegraphics" in line:
            include_section = any(item in selected_components for item in ["Tables", "Figures"])

        if include_section:
            filtered_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(filtered_lines)

    print(f"Modified LaTeX file saved as {output_file}")

def compile_latex_to_pdf(tex_file):
    try:
        subprocess.run(["pdflatex", tex_file], check=True)
        print("PDF successfully generated!")
    except subprocess.CalledProcessError as e:
        print("Error in LaTeX compilation:", e)

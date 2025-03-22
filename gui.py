import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem, QFileDialog
)


class LaTeXReportGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LaTeX Report Generator")
        self.setGeometry(100, 100, 600, 400)

        # Layout
        self.layout = QVBoxLayout()

        # Load File Button
        self.load_button = QPushButton("Load .tex File")
        self.load_button.clicked.connect(self.load_tex_file)
        self.layout.addWidget(self.load_button)

        # List Widget for Sections
        self.section_list = QListWidget()
        self.section_list.setSelectionMode(QListWidget.MultiSelection)
        self.layout.addWidget(self.section_list)

        # Generate PDF Button
        self.generate_button = QPushButton("Generate PDF")
        self.generate_button.clicked.connect(self.generate_pdf)
        self.layout.addWidget(self.generate_button)

        # Status Label
        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)
        self.tex_file_path = None
        self.sections = []

    def load_tex_file(self):
        """Load the LaTeX file and extract sections."""
        options = QFileDialog.Options()
        self.tex_file_path, _ = QFileDialog.getOpenFileName(self, "Select LaTeX File", "", "TeX Files (*.tex)", options=options)

        if self.tex_file_path:
            self.status_label.setText(f"Loaded: {os.path.basename(self.tex_file_path)}")
            self.extract_sections()

    def extract_sections(self):
        """Extract sections from the LaTeX file."""
        self.sections.clear()
        self.section_list.clear()

        with open(self.tex_file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        current_section = []
        section_name = None

        for line in lines:
            if line.strip().startswith(r"\section{") or line.strip().startswith(r"\subsection{"):
                if section_name:  # Save previous section
                    self.sections.append((section_name, current_section))
                section_name = line.strip()
                current_section = [line]
            else:
                current_section.append(line)

        if section_name:  # Save last section
            self.sections.append((section_name, current_section))

        # Add sections to the list widget
        for section, _ in self.sections:
            item = QListWidgetItem(section)
            self.section_list.addItem(item)

    def generate_pdf(self):
        """Generate PDF with selected sections."""
        if not self.tex_file_path:
            self.status_label.setText("No LaTeX file loaded!")
            return

        selected_items = self.section_list.selectedItems()
        if not selected_items:
            self.status_label.setText("No sections selected!")
            return

        selected_sections = {item.text() for item in selected_items}
        output_tex_path = "output/filtered_report.tex"

        with open(output_tex_path, "w", encoding="utf-8") as output_file:
            with open(self.tex_file_path, "r", encoding="utf-8") as input_file:
                include = True
                for line in input_file:
                    if line.strip().startswith(r"\section{") or line.strip().startswith(r"\subsection{"):
                        include = line.strip() in selected_sections
                    if include:
                        output_file.write(line)

        # Compile LaTeX file to PDF
        self.compile_latex(output_tex_path)

    def compile_latex(self, tex_file):
        """Run pdflatex to compile the LaTeX file into a PDF."""
        try:
            subprocess.run(["pdflatex", "-output-directory=output", tex_file], check=True)
            self.status_label.setText("PDF successfully generated!")
        except subprocess.CalledProcessError:
            self.status_label.setText("Error in LaTeX compilation.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaTeXReportGenerator()
    window.show()
    sys.exit(app.exec_())

from setuptools import setup, find_packages

# Read long description from README.md
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "2print (also known as toprint) - A comprehensive printing solution for HTML, PDF, ZPL, and image formats with printer support. Perfect for converting and printing documents in various formats including HTML to PDF, PDF to print, ZPL label printing, and image processing."

setup(
    name="toprint",
    version="0.1.29",
    description="2print/toprint: Python library for printing and converting between HTML, PDF, ZPL, and image formats with printer support. Also known as 2print or to-print.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tom Softreck",
    author_email="info@softreck.dev",
    url="https://github.com/text2doc/toPrint",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    keywords=[
        # Podstawowe słowa kluczowe
        'printing', 'pdf', 'html', 'zpl', 'label', 'printer', 'conversion',
        # Warianty z 2 dla lepszego wyszukiwania
        '2print', '2-print', 'print2', 'print-2',
        # Konwersje między formatami
        'html2pdf', 'pdf2print', 'zpl2print', 'image2print',
        'html-to-pdf', 'pdf-to-print', 'zpl-to-print', 'image-to-print',
        # Dodatkowe słowa kluczowe
        'document', 'report', 'label-printing', 'barcode', 'qrcode',
        'thermal-printing', 'document-generation', 'report-generation',
        'zebra', 'zpl-printer', 'weasyprint', 'pdf-generation',
        'print-to-pdf', 'thermal-print', 'label-maker', 'document-conversion'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Printing',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Office/Business :: Office Suites',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.7",
    install_requires=[
        'weasyprint>=53.0',
        'Pillow>=8.0.0',
        'reportlab>=3.6.0',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/text2doc/toPrint/issues',
        'Source': 'https://github.com/text2doc/toPrint',
        'Documentation': 'https://github.com/text2doc/toPrint#readme',
        'Changelog': 'https://github.com/text2doc/toPrint/releases',
    },
    entry_points={
        'console_scripts': [
            'to-print=toPrint.cli:main',
        ],
    },
)

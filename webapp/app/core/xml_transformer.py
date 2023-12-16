import os
from lxml import etree
from app.config import BASE_DIR, DOWNLOAD_DIR


class XmlTransformer:
    def transform(self):
        xml_file = os.path.join(DOWNLOAD_DIR, "test.xml")
        xml_tree = etree.parse(xml_file)

        xslt_file = os.path.join(BASE_DIR, "static/transform.xslt")
        xslt_tree = etree.parse(xslt_file)

        transform = etree.XSLT(xslt_tree)

        # Apply the XSLT transformation to the XML
        return transform(xml_tree)

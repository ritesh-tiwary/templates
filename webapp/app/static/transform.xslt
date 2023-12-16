<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <!-- Define the transformation here -->
    <html>
      <body>
        <h2>Transformed XML</h2>
        <xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>

  <!-- Add more templates as needed for your transformation -->

</xsl:stylesheet>

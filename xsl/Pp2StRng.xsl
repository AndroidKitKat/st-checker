<?xml version="1.0" encoding="utf-8"?>
<!--
    Stylesheet for Protection Profile Schema
    Based on original work by Dennis Orth
    Subsequent modifications in support of US NIAP
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:cc="https://niap-ccevs.org/cc/v1"
  version="1.0">

  <!-- release variable, overridden to "final" for release versions -->
  <xsl:template match="/cc:PP">

    <grammar ns="https://niap-ccevs.org/cc/v1"
	     xmlns="http://relaxng.org/ns/structure/1.0"
	     datatypeLibrary="http://www.w3.org/2001/XMLSchema-datatypes"
	     xmlns:htm="http://www.w3.org/1999/xhtml"
	     xmlns:a="http://relaxng.org/ns/compatibility/annotations/1.0"
	     >
    </grammar>


    
  </xsl:template>
</xsl:stylesheet>

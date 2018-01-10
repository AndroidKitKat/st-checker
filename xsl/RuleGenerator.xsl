<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fo="http://www.w3.org/1999/XSL/Format"
    xmlns:axsl="http://www.w3.org/1999/XSL/TransformAlias"
    xmlns:cc="https://niap-ccevs.org/cc/v1"
    >

  <xsl:namespace-alias stylesheet-prefix="axsl" result-prefix="xsl"/>
  
  <xsl:template match="/">
    <axsl:stylesheet version="1.0">
      <axsl:template match="/">
	<xsl:for-each select="//cc:f-element|//cc:a-element">
	  <axsl:choose>
	    <axsl:when test="//*[@id='{@id}']">
	    </axsl:when>
	    <axsl:otherwise>
	      <axsl:message terminate="yes">
		Missing <xsl:value-of select="@id"/>.
	      </axsl:message>
	    </axsl:otherwise>
	  </axsl:choose>
	</xsl:for-each>
      </axsl:template>
    </axsl:stylesheet>
  </xsl:template>
</xsl:stylesheet>

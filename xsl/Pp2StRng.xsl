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

    <grammar ns="https://niap-ccevs.org/cc/st/v1"
	     xmlns="http://relaxng.org/ns/structure/1.0"
	     datatypeLibrary="http://www.w3.org/2001/XMLSchema-datatypes"
	     xmlns:htm="http://www.w3.org/1999/xhtml"
	     xmlns:a="http://relaxng.org/ns/compatibility/annotations/1.0"
	     >
      <start>
	<element name="security-target">
	  <a:documentation>Root element for a Security Target XML document</a:documentation>
	</element>


	<element name="SecurityFunctionRequirements">
	  <xsl:for-each select=".//*[cc:f-component]">
	    <element name="component">
	      <attribute name="id">
	      <xsl:for-each select="cc:f-component">
		<element name="element">
		  <xsl:for-each select="cc:f-element">
		    
		    <xsl:apply-templates select="cc:title"/>
		  </xsl:for-each>
		</element>
	      </xsl:for-each>
	    </element>
	  </xsl:for-each>
	</element>
      </start>




      <define name="basic-content">
	<a:documentation>
	  Content that can go anywhere.
	</a:documentation>
	<oneOrMore>
	  <choice>
	    <text/>
	    <ref name="html-element"/>
	  </choice>
	</oneOrMore>
      </define>


    </grammar>
  </xsl:template>


  <xsl:template match="cc:f-component | cc:a-component">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- Unwrap and descend elements by default -->
  <xsl:template match="*">
    <xsl:apply-templates/>
  </xsl:template>

  <!-- <\!- - Gobble up text by default -\-> -->
  <!-- <xsl:template match="text()"/> -->

  <!-- <\!- - Gobble up text by default -\-> -->
  <!-- <xsl:template match="text()" mode="showtext"> -->
  <!--   <xsl:value-of select="text()"/> -->
  <!-- </xsl:template> -->

  
</xsl:stylesheet>

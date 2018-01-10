import re

#regex=r".*"
regex=r"TheOSshallimplementtherequirementsinTLS\(FCS_TLSC_EXT.1\)fortheDTLSimplementation,exceptwherevariationsareallowedaccordingtoDTLS1\.2\(RFC6347\)\."


#regex=r"TheOSshallgenerateasymmetriccryptographickeysinaccordancewithaspecifiedcryptographickeygenerationalgorithm\[((RSAschemesusingcryptographickeysizesof2048-bitorgreaterthatmeetthefollowing\:FIPSPUB186-4,“DigitalSignatureStandard\(DSS\)”,AppendixB\.3|ECCschemesusing“NISTcurves”P-256,P-384and\[((P-521|noothercurves)\,?)+\]thatmeetthefollowing\:FIPSPUB186-4,“DigitalSignatureStandard\(DSS\)”,AppendixB\.4|P-521|noothercurves|FFCschemesusingcryptographickeysizesof2048-bitorgreaterthatmeetthefollowing\:FIPSPUB186-4,“DigitalSignatureStandard\(DSS\)”,AppendixB\.1)\,?)+\]\."

text=r"""	  The OS shall implement the requirements in TLS (<linkref linkend="FCS_TLSC_EXT.1"/>) for the DTLS implementation, except where variations are allowed according to DTLS 1.2 (RFC 6347).
"""


text=r"""[ P-521 ]
"""

if re.match(regex+".*", re.sub(r'\s+', '', text)) :
    print("Match")

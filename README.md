# TCC | Piano Playing Robot

- Conversor de partitura para XML: [github.com/BreezeWhite/oemer](https://github.com/BreezeWhite/oemer)
- Exemplo de partitura em XML: [www.w3.org/2021/06/musicxml40/tutorial/introduction/](https://www.w3.org/2021/06/musicxml40/tutorial/introduction/)
- Converter XML para C++: [linuxhint.com/parse_xml_in_cpp/](https://linuxhint.com/parse_xml_in_cpp/)
- Tocar arquivos **.xml** online: [freetomik.github.io](https://freetomik.github.io)
- Software para tocar arquivos **.musicxml**: [https://www.nch.com.au/notation/index.html](https://www.nch.com.au/notation/index.html)

## Estrutura do XML
``` xml
<measure number="1"> <!-- compasso 1 -->
    <attributes>
        <divisions>16</divisions>
        <key>
            <fifths>0</fifths>
        </key>
        <staves>1</staves>
        <clef number="1"> <!-- clave 1 -->
            <sign>G</sign> <!-- sol -->
            <line>2</line> <!-- inicia na linha 2 -->
        </clef>
    </attributes>
    <note> <!-- nota -->
        <pitch>
            <step>F</step> <!-- fá -->
            <alter>0</alter>
            <octave>4</octave> <!-- oitava 4 -->
        </pitch>
        <duration>8</duration> <!-- duração 8 -->
        <type>eighth</type> <!-- colcheia -->
        <stem>up</stem> <!-- haste subindo -->
        <staff>1</staff>
        <voice>1</voice>
    </note>
    <note>
        <pitch>
            <step>G</step> <!-- sol -->
            <alter>0</alter>
            <octave>4</octave> <!-- oitava 4 -->
        </pitch>
        <duration>8</duration> <!-- duração 8 -->
        <type>eighth</type> <!-- colcheia -->
        <stem>up</stem> <!-- haste subindo -->
        <staff>1</staff>
        <voice>1</voice>
    </note>
</measure>
```
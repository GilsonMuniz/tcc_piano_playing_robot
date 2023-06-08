# TCC | Piano Playing Robot

- Conversor de partitura para XML: [github.com/BreezeWhite/oemer](https://github.com/BreezeWhite/oemer)
- Exemplo de partitura em XML: [www.w3.org/2021/06/musicxml40/tutorial/introduction/](https://www.w3.org/2021/06/musicxml40/tutorial/introduction/)
- Converter XML para C++: [linuxhint.com/parse_xml_in_cpp/](https://linuxhint.com/parse_xml_in_cpp/)
- Tocar arquivos **.xml** online: [freetomik.github.io](https://freetomik.github.io), [soundslice.com/musicxml-viewer](https://www.soundslice.com/musicxml-viewer/)
- Software para tocar arquivos **.musicxml**: [https://www.nch.com.au/notation/index.html](https://www.nch.com.au/notation/index.html)

## Estrutura do **XML**
`titanic.xml`
``` xml
<measure number="1"> <!-- compasso 1 -->
    <attributes>
        <divisions>16</divisions>
        <key>
            <fifths>0</fifths> <!-- (+) sustenidos na armadura de clave -->
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
            <alter>0</alter> <!-- (+) sustenido na nota -->
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
<measure number="16">
    <note>
        <rest measure="yes"/> <!-- pausa -->
        <duration>24</duration>
        <dot/> <!-- ponto de aumento -->
        <staff>1</staff>
    </note>
</measure>
<measure number="19">
    ...
    <note>
        <pitch>
            <step>B</step>
            <alter>-1</alter> <!-- (-) bemol na nota -->
            <octave>4</octave>
        </pitch>
        <duration>16</duration>
        <type>quarter</type>
        <stem>down</stem>
        <staff>1</staff>
        <voice>1</voice>
    </note>
    ...
```

## Estrutura do **XLSX**
Após ser executado o script Python para tradução do arquivo XML, é gerada uma tabela que contém 3 colunas, que será lida pelo microcontrolador.
Cada linha da matriz, representa uma nota a ser tocada na música, sendo representada pelas 3 células que a definem: **Step**, **Octave** e **Duration**.
- **Step** define a [cifra](https://pt.wikipedia.org/wiki/Cifra_(música));
- **Octave** representa a [oitava](https://pt.wikipedia.org/wiki/Oitava);
- **Duration** indica o tempo de duração da nota;

Exemplo de tabela gerada:

| Step | Octave | Duration |
|------|--------|----------|
| F    | 4      | 8        |
| G    | 4      | 8        |
| A    | 4      | 48       |
| G    | 4      | 8        |
| F    | 4      | 8        |
| G    | 4      | 16       |
| C    | 5      | 32       |
| B    | 4      | 8        |
| A    | 4      | 8        |
| F    | 4      | 16       |
| D    | 4      | 16       |
| ...  | ...    | ...      |
| D    | 4      | 64       |

## Tipos de nota
<img src="docs\notes-values.png" width="260">
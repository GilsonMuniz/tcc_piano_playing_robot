# TCC | Piano Playing Robot

- Conversor de partitura para XML: [github.com/BreezeWhite/oemer](https://github.com/BreezeWhite/oemer)
- Exemplo de partitura em XML: [www.w3.org/2021/06/musicxml40/tutorial/introduction](https://www.w3.org/2021/06/musicxml40/tutorial/introduction/)
- Tocar arquivos **.xml** e **.musicxml** online: [soundslice.com/musicxml-viewer](https://www.soundslice.com/musicxml-viewer/)
- Software para tocar **.musicxml**: [musescore.org/en/download](https://musescore.org/en/download)
- Apresentação do projeto: [bit.ly/PianoPlayingRobot](https://bit.ly/PianoPlayingRobot)

## Estrutura do **XML**
``` xml
<!-- titanic.xml -->

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
    <!-- ... -->
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
    <!-- ... -->
<!-- ... -->
```
``` xml
<!-- cidade_maravilhosa.xml -->

<!-- ... -->
<measure number="3">
    <note>
        <pitch>
            <step>E</step>
            <alter>0</alter>
            <octave>5</octave>
        </pitch>
        <duration>32</duration>
        <type>half</type>
        <stem>down</stem>
        <staff>1</staff>
        <voice>1</voice>
    </note>
    <note>
        <chord/> <!-- acorde com a última nota -->
        <pitch>
            <step>C</step>
            <alter>0</alter>
            <octave>5</octave>
        </pitch>
        <duration>32</duration>
        <type>half</type>
        <stem>down</stem>
        <staff>1</staff>
        <voice>1</voice>
    </note>
</measure>
<!-- ... -->

```

## Estrutura do **XLSX**
Após ser executado o script Python para tradução do arquivo XML, é gerada uma tabela que contém 128 colunas, que será lida pelo microcontrolador.
A tabela funciona como uma matriz, em que sua primeira coluna "**Sample** "indica o instante atual de tempo, sendo iniciada em 0 e terminando no tempo de duração da música. As colunas restantes, representam o estado de cada nota ou pausa naquele ponto da música, podendo ser _True_ ou _False_. A última coluna, **Rest**, representa a presença de pausa.
Para tocar a música, o robô deverá ler linha por linha em ordem crescente conforme as amostras, e acionar as saídas digitais do microcontrolador conforme a tabela de notas e a pausa. Caso a célula lida seja _True_, será pressionada a tecla, caso contrário, não.

- **Step** define a [cifra](https://pt.wikipedia.org/wiki/Cifra_(música)), podendo ser acrescentado **'#'** ou **'b'** após a letra, para indicar [sustenido](https://pt.wikipedia.org/wiki/Sustenido) e [bemol](https://pt.wikipedia.org/wiki/Bemol), respectivamente;
- **Octave** representa a [oitava](https://pt.wikipedia.org/wiki/Oitava);
- **Chord** indica se a nota compõe um [acorde](https://pt.wikipedia.org/wiki/Acorde);
- **Duration** é o tempo de duração da nota.

Exemplo de tabela gerada:

| Sample | C1 | C#1 | Db1 | D1 | D#1 | Eb1  | E1 | Fb1 | E#1 | F1 | F#1 | Gb1 | G1 | G#1  | Ab1 | A1 | A#1 | Bb1 | B1 | Cb1 | B#1 | ... | Rest |
|--------|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|-----|------|
| 1      |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |     | True |
| 2      |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |     | True |
| 3      |    |     |     |    |     | True |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |     | True |
| 4      |    |     |     |    |     | True |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |     | True |
| 5      |    |     |     |    |     | True |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |     |      |
| 6      |    |     |     |    |     | True |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |     |      |
| 7      |    |     |     |    |     |      |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |     |      |
| 8      |    |     |     |    |     |      |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |     |      |

## Tipos de nota
| Symbol                                             | Name               | Duration |
|----------------------------------------------------|--------------------|----------|
| <img src="docs\semibreve.svg" width="50">          | Semibreve          | 64       |
| <img src="docs\minim.svg" width="50">              | Minim              | 32       |
| <img src="docs\crotchet.svg" width="50">           | Crotchet           | 16       |
| <img src="docs\quaver.svg" width="50">             | Quaver             | 08       |
| <img src="docs\semiquaver.svg" width="50">         | Semiquaver         | 04       |
| <img src="docs\demisemiquaver.svg" width="50">     | Demisemiquaver     | 02       |
| <img src="docs\hemidemisemiquaver.svg" width="50"> | Hemidemisemiquaver | 01       |

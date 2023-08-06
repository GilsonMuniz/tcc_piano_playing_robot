# TCC | Piano Playing Robot

- Conversor de partitura para XML: [github.com/BreezeWhite/oemer](https://github.com/BreezeWhite/oemer)
- Exemplo de partitura em XML: [www.w3.org/2021/06/musicxml40/tutorial/introduction](https://www.w3.org/2021/06/musicxml40/tutorial/introduction/)
- Tocar arquivos **.xml** e **.musicxml** online: [soundslice.com/musicxml-viewer](https://www.soundslice.com/musicxml-viewer/)
- Software para tocar **.musicxml**: [musescore.org/en/download](https://musescore.org/en/download)
- Apresentação do projeto: [bit.ly/PianoPlayingRobot](https://bit.ly/PianoPlayingRobot)

## Estrutura do **XML**

### Compasso | Measure
Contém as tags note e backup.
- Note: nota ou pausa;
- Backup: recuar determinado tempo ou valor no compasso.
``` xml
<measure number="1">
    <note></note>
    <note></note>
    <backup></backup>
    <note></note>
    <backup></backup>
    <note></note>
</measure>
```

### Nota ou Pausa | Note
Contém as tags pitch, duration, type, stem, staff e voice.
1. Pitch: indica a cifra da nota, se existe acidente e qual e a oitava;
2. Duration: duração da nota;
3. Type: tipo da nota conforme a [tabela](https://github.com/gilsonmuniz/tcc_piano_playing_robot#tipos-de-nota-e-pausas);
4. Stem: haste da nota para cima ou para baixo;
5. Staff: _
6. Voice: _
``` xml
<note>
    <pitch></pitch>
    <duration>32</duration>
    <type>half</type>
    <stem>down</stem>
    <staff>1</staff>
    <voice>1</voice>
</note>
```

### Pitch
Contém as tags step, alter e octave.
1. Step: cifra da nota;
2. Alter: valor inteiro para indicar se há acidente e qual é;
3. Octave: oitava da nota.
``` xml
<pitch>
    <step>E</step>
    <alter>0</alter>
    <octave>5</octave>
</pitch>
```

## Estrutura do **XLSX**
Após ser executado o script Python para tradução do arquivo XML, é gerada uma tabela que contém 128 colunas, que será lida pelo microcontrolador.
A tabela funciona como uma matriz, em que sua primeira coluna "**Sample** "indica o instante atual de tempo, sendo iniciada em 0 e terminando no tempo de duração da música. As colunas restantes, representam o estado de cada nota ou pausa naquele ponto da música, podendo ser _True_ ou _False_. A última coluna, **Rest**, representa a presença de pausa.
Para tocar a música, o robô deverá ler linha por linha em ordem crescente conforme as amostras, e acionar as saídas digitais do microcontrolador conforme a tabela de notas e a pausa. Caso a célula lida seja _True_, será pressionada a tecla, caso contrário, não.

- **Step** define a [cifra](https://pt.wikipedia.org/wiki/Cifra_(música)), podendo ser acrescentado **'#'** ou **'b'** após a letra, para indicar [sustenido](https://pt.wikipedia.org/wiki/Sustenido) e [bemol](https://pt.wikipedia.org/wiki/Bemol), respectivamente;
- **Octave** representa a [oitava](https://pt.wikipedia.org/wiki/Oitava);
- **Chord** indica se a nota compõe um [acorde](https://pt.wikipedia.org/wiki/Acorde);
- **Duration** é o tempo de duração da nota.

### Exemplo de tabela gerada

| Sample | C1 | C#1 | Db1 | D1 | D#1 | Eb1  | E1 | Fb1 | E#1 | F1 | F#1 | Gb1 | G1 | G#1  | Ab1 | A1 | A#1 | Bb1 | B1 | Cb1 | B#1 | C2 | C#2 | Db2 | D2 | D#2 | Eb2  | E2 | Fb2 | E#2 | F2 | F#2 | Gb2 | G2 | G#2  | Ab2 | A2 | A#2 | Bb2 | B2 | Cb2 | B#2 | C3 | C#3 | Db3 | D3 | D#3 | Eb3  | E3 | Fb3 | E#3 | F3 | F#3 | Gb3 | G3 | G#3  | Ab3 | A3 | A#3 | Bb3 | B3 | Cb3 | B#3 | C4 | C#4 | Db4 | D4 | D#4 | Eb4  | E4 | Fb4 | E#4 | F4 | F#4 | Gb4 | G4 | G#4  | Ab4 | A4 | A#4 | Bb4 | B4 | Cb4 | B#4 | C5 | C#5 | Db5 | D5 | D#5 | Eb5  | E5 | Fb5 | E#5 | F5 | F#5 | Gb5 | G5 | G#5  | Ab5 | A5 | A#5 | Bb5 | B5 | Cb5 | B#5 | C6 | C#6 | Db6 | D6 | D#6 | Eb6  | E6 | Fb6 | E#6 | F6 | F#6 | Gb6 | G6 | G#6  | Ab6 | A6 | A#6 | Bb6 | B6 | Cb6 | B#6 | Rest |
|--------|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|----|-----|-----|----|-----|------|----|-----|-----|----|-----|-----|----|------|-----|----|-----|-----|----|-----|-----|------|
| 1      |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 2      |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 3      |    |     |     |    |     | True |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 4      |    |     |     |    |     | True |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 5      |    |     |     |    |     | True |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 6      |    |     |     |    |     | True |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 7      |    |     |     |    |     |      |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |
| 8      |    |     |     |    |     |      |    |     |     |    |     |     |    | True |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |    |     |     |    |     |      |    |     |     |    |     |     |    |      |     |    |     |     |    |     |     |      |

## Tipos de nota e pausas
| Name               | Note Symbol                                        | Rest Symbol                                            | Duration |
|--------------------|----------------------------------------------------|--------------------------------------------------------|----------|
| Semibreve          | <img src="docs\semibreve.svg" width="50">          | <img src="docs\semibreverest.svg" width="50">          | 64       |
| Minim              | <img src="docs\minim.svg" width="50">              | <img src="docs\minimrest.svg" width="50">              | 32       |
| Crotchet           | <img src="docs\crotchet.svg" width="50">           | <img src="docs\crotchetrest.svg" width="50">           | 16       |
| Quaver             | <img src="docs\quaver.svg" width="50">             | <img src="docs\quaverrest.svg" width="50">             | 08       |
| Semiquaver         | <img src="docs\semiquaver.svg" width="50">         | <img src="docs\semiquaverrest.svg" width="50">         | 04       |
| Demisemiquaver     | <img src="docs\demisemiquaver.svg" width="50">     | <img src="docs\demisemiquaverrest.svg" width="50">     | 02       |
| Hemidemisemiquaver | <img src="docs\hemidemisemiquaver.svg" width="50"> | <img src="docs\hemidemisemiquaverrest.svg" width="50"> | 01       |

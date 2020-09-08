# [SudokuAlly](https://github.com/matejbolta/SudokuAlly)
##### Projektna naloga pri predmetu [Uvod v programiranje](https://github.com/matijapretnar/uvod-v-programiranje) na __[Fakulteti za matematiko in fiziko](https://www.fmf.uni-lj.si/si/)__.
![Grid](https://qph.fs.quoracdn.net/main-qimg-bd9c2c0ab60b01af87f135939d847684.webp)
### Uvod
Sudoku je logična uganka, katere cilj je zapolniti kvadratno mrežo velikosti 9 x 9, s števili med 1 in 9.
Vsako število se lahko pojavi točno enkrat v vsaki vrstici, vsakem stolpcu in v vsakem manjšem kvadratu velikosti 3 x 3.

### Opis
Če ste kdaj reševali sudoku in niste uspeli priti do konca, bo SudokuAlly kot nalašč za vas. Na poti do pravilne rešitve vam pomaga na različne načine in vas tako vedno varno pripelje do zaključene uganke.

*Opomba: program prvotno ni namenjen igranju igre sudoku, saj vam sam ne ponudi začetne mreže. Vanj vnesete svojo mrežo (ki je ne znate rešiti), on pa vam pomaga na poti do rešitve. Primer uporabe: v reviji rešujete sudoku, pri katerem ne pridete do končnega stanja. Mrežo vnesete v SudokuAlly, ta pa vam pomaga na poti do rešitve.*

### Zaganjanje programa
Na [povezavi](https://github.com/matejbolta/SudokuAlly) izberite "Code" in nato "Download ZIP" (ali uporabite GIT). Po prenosu mapo razširite (unzip) in jo odprite v izbranem urejevalniku besedila (npr: [Visual Studio Code](https://code.visualstudio.com/)). Nato v ukazni vrstici poženite datoteko "SudokuAlly.py". Na [povezavi](http://127.0.0.1:8080/) se vam bo odprla začetna stran programa. V primeru težav v izbrani brskalnik prilepite URL: http://127.0.0.1:8080/ ali http://localhost:8080/

### Kako program deluje
Po uspešnem zagonu programa v meniju izberete vnos nove mreže in jo (pravilno!) vnesete. V primeru, da vnašate zelo težko mrežo se lahko zgodi, da se bo naslednja stran nalagala nekaj sekund. Bodite potrpežljivi. Nato sledite intuitivnemu reševanju mreže. Številke lahko vnašate sami, ponujeni pa so vam tudi različni načini pomoči. SudokuAlly vam na zahtevo reši točno določeno polje v mreži, naključno polje v mreži ali celotno mrežo.
Vse vnesene mreže se vam tudi shranjujejo. Če med reševanjem program zaprete, bo dostop do vseh vnesenih mrež še vedno dostopen ob naslednjem obisku programa. Uživajte!

*Opomba: pri vnosu mreže bodite prepričani, da ima vnesena mreža le eno rešitev (vse mreže, ki jih najdete na internetu, v knjigah, revijah ali časopisu, imajo le eno rešitev). V primeru, da bo rešitev več, bo SudokuAlly za "pravo rešitev" izbral le eno izmed vseh možnih.*
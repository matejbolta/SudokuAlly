% import model
% rebase('base.tpl')

<blockquote>
    <h3>{{ime}}</h3>
</blockquote>

<blockquote>
    <pre>{{mreza}}</pre>
</blockquote>

<blockquote>
    <h3>{{stanje}}</h3>
</blockquote>

<br><br><br>

<!-- Gumbi, po vrsti za:
    Vnesi številko,
    Reši to polje,
    Reši naključno polje,
    Reši celotno mrežo,
    Shrani & Domov. -->
    <table>
        <tr>
            <td>
                <form action="/poskus_namig/vnesi_stevilko/" method="POST">
                    Vrsta: <input size="1" type="text", name="vrsta", maxlength="1">
                    Stolpec: <input size="1" type="text", name="stolpec", maxlength="1">
                    Število: <input size="1" type="text", name="stevilo", maxlength="1">
                    <button type="submit">Vnesi številko</button>
                </form>
            </td>
        </tr>
        <tr>
            <td>
                <form action="/poskus_namig/resi_polje/" method="POST">
                    Vrsta: <input size="1" type="text", name="vrsta", maxlength="1">
                    Stolpec: <input size="1" type="text", name="stolpec", maxlength="1">
                    <button type="submit">Reši to polje</button>
                </form>
            </td>
        </tr>
        <tr>
            <td>
                <form action="/poskus_namig/resi_nakljucno/" method="POST">
                    <button type="submit">Reši naključno polje</button>
                </form>
            </td>
            <td>
                <form action="/poskus_namig/resi_vse/" method="POST">
                    <button type="submit">Reši celotno mrežo</button>
                </form>
            </td>
            <td>
                <form action="/SudokuAlly/" method="GET">
                    <button type="submit">Shrani & Domov</button>
                </form>
            </td>
        </tr>
        <tr>
            <td>
                <form action="/poskus_namig/izbris_mreze/" method="POST">
                    <button type="submit">Izbriši to mrežo</button>
                </form>
            </td>
        </tr>
    </table>
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

<table>
    <tr>
        <td>
            <form action="/nova_mreza/" method="get">
                <button type="submit">Nova mreža</button>
            </form>
        </td>
        <td>
            <form action="/odprte_mreze/" method="get">
                <button type="menu">Že obstoječa mreža</button>
            </form>
        </td>
        <td>
            <form action="/statistika/" method="post">
                <button type="submit">Statistika</button>
            </form>
        </td>
    </tr>
</table>
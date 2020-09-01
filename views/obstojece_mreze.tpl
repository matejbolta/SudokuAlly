% import model
% rebase('base.tpl')

<table>
    <tr>
        <td>
            <strong>
                Izberite željeno mrežo.
            </strong>
        </td>
    </tr>
    <tr>
        <form action="/SudokuAlly/" method="GET">
            <button type="submit">Domov</button>
        </form>
    </tr>
    <br>
    % for ime in sudokually.mreze.keys():
    <tr>
        <td>
            <form action="/obstojece_mreze/{{ime}}/" method="POST">
                <button type="submit">{{ime}}</button>
            </form>
        </td>
    </tr>
    % end
</table>
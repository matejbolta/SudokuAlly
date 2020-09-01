% import model
% rebase('base.tpl')

<blockquote>
  <h5>SudokuAlly - vaš zaveznik, ko številke postanejo prezahtevne.</h5>
</blockquote>

<table>
  <tr>
    <td>
      <form action="/nova_mreza/" method="get">
        <button type="submit">Nova mreža</button>
      </form>
    </td>
    
    <td>
      <form action="/obstojece_mreze/" method="get">
        <button type="submit">Že obstoječa mreža</button>
      </form>
    </td>
    
    <td>
      <form action="/statistika/" method="post">
        <button type="submit">Statistika</button>
      </form>
    </td>
  </tr>
</table>

<img src="/img/sudoku.gif" alt="picture">
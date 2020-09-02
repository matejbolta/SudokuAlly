% import model
% rebase('base.tpl')

<style>
  button { margin:5px 12px 0px 30px; }
</style>

<blockquote>
  <h4><i>SudokuAlly - vaš zaveznik, ko številke postanejo prezahtevne.</i></h4>
</blockquote>

<table>
  <tr>
    <td>
      <form action="/nova_mreza/" method="GET">
        <button type="submit">DODAJ MREŽO</button>
      </form>
    </td>
    
    <td>
      <form action="/obstojece_mreze/" method="GET">
        <button type="submit">OBSTOJEČA MREŽA</button>
      </form>
    </td>
    
    <td>
      <form action="/statistika/" method="GET">
        <button type="submit">STATISTIKA</button>
      </form>
    </td>
  </tr>
</table>

<img src="/img/sudoku.gif" alt="picture">
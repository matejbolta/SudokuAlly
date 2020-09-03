% import model
% rebase('base.tpl')


<h4 style="margin-left:42px;"><i>SudokuAlly - vaš zaveznik, ko številke postanejo prezahtevne.</i></h4>

<table>
  <tr>
    <td>
      <form action="/nova_mreza/" method="GET">
        <button style="margin-left:46px" type="submit">DODAJ MREŽO</button>
      </form>
    </td>
    
    <td>
      <form action="/obstojece_mreze/" method="GET">
        <button style="margin-left:27px" type="submit">OBSTOJEČA MREŽA</button>
      </form>
    </td>
    
    <td>
      <form action="/statistika/" method="GET">
        <button style="margin-left:27px" type="submit">STATISTIKA</button>
      </form>
    </td>
  </tr>
</table>

<img src="/img/sudoku.gif" alt="picture">
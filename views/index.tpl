% import model
% rebase('base.tpl')

<h4 style="margin-top:15px;margin-bottom:31px;">SudokuAlly - vaš zaveznik, ko številke postanejo prezahtevne.</h4>

<table>
  <tr>
    <td>
      <form action="/SudokuAlly/nova_mreza/" method="GET">
        <button type="submit">DODAJ MREŽO</button>
      </form>
    </td>
    
    <td>
      <form action="/SudokuAlly/obstojece_mreze/" method="GET">
        <button type="submit">OBSTOJEČA MREŽA</button>
      </form>
    </td>
    
    <td>
      <form action="/SudokuAlly/statistika/" method="GET">
        <button type="submit">STATISTIKA</button>
      </form>
    </td>
  </tr>
</table>

<img src="/SudokuAlly/img/index.gif" alt="picture" height="380px">
% import model
% rebase('base.tpl')

<style>
    #mreze { border-collapse: collapse; width: 190px; }
    
    #mreze td, #mreze th { border: 1px solid #ddd; padding: 5px; }
    
    #mreze tr:nth-child(even){ background-color: #f2f2f2; }
    
    #mreze tr:hover { background-color: #ddd; }
    
    #mreze th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: #50d5e9;
        color: white;
    }
    
    table { display: inline-table; }

    h4 { color:#e9b04e; margin-top:50px; margin-bottom:0px; }
</style>

% if not sudokually.mreze:
<h4><strong>Trenutno ni obstoječih mrež!</strong></h4> <br><br>

<form action="/SudokuAlly/" method="GET">
    <button type="submit">DOMOV</button>
</form>

% else:
<br>
<div id="outerdiv">
    <table class="leva" id="mreze">
        <tr>
            <th>
                Odprte mreže:
            </th>
        </tr>
        % for ime, (_, stanje) in sudokually.mreze.items():
        % if not (stanje == model.RESEN_SUDOKU):
        <tr>
            <td>
                <form action="/SudokuAlly/obstojece_mreze/{{ime}}/" method="POST">
                    <button style="margin:auto;background-color:#e9b04e;color:white;padding:6px;font-size:11px;" type="submit">{{ime}}</button>
                </form>
            </td>
        </tr>
        % end
        % end
    </table>
    
    <table class="desna" id="mreze">
        <tr>
            <th>
                Rešene mreže:
            </th>
        </tr>
        % for ime, (_, stanje) in sudokually.mreze.items():
        % if stanje == model.RESEN_SUDOKU:
        <tr>
            <td>
                <form action="/SudokuAlly/obstojece_mreze/{{ime}}/" method="POST">
                    <button style="margin:auto;background-color:#e9b04e;color:white;padding:6px;font-size:11px;" type="submit">{{ime}}</button>
                </form>
            </td>
        </tr>
        % end
        % end
    </table>
</div><br>

<section class="container">
    <form action="/SudokuAlly/" method="get">
        <button style="margin-left:335px" type="submit">DOMOV</button>
    </form>
</section>
% end
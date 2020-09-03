% import model
% rebase('base.tpl')

<style>
    #mreze {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 200px;
        margin-left:5px
    }
    
    #mreze td, #mreze th {
        border: 1px solid #ddd;
        padding: 5px;
    }
    
    #mreze tr:nth-child(even){background-color: #f2f2f2;}
    
    #mreze tr:hover {background-color: #ddd;}
    
    #mreze th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: #50d5e9;
        color: white;
    }
</style>

% if not sudokually.mreze:
<style>
    button { margin:0px 0px 0px 197px; }
    h4 {
        margin:0px 0px 0px 122px;
        padding: 0.5em 10px;
    }
</style>

<h4>
    <strong>
        Trenutno ni obstoječih mrež!
    </strong>
</h4>
<br><br>
<form action="/SudokuAlly/" method="GET">
    <button type="submit">DOMOV</button>
</form>

% elif sudokually.odprte_resene()[0] <= sudokually.odprte_resene()[1]:
<section class="container">
    <div style="float: left;margin-left:25px;margin-right:33px">
        <table id="mreze">
            <tr>
                <th>
                    Odprte mreže:
                </th>
            </tr>
            % for ime, (_, stanje) in sudokually.mreze.items():
            % if not (stanje == model.RESEN_SUDOKU):
            <tr>
                <td>
                    <form action="/obstojece_mreze/{{ime}}/" method="POST">
                        <button style="margin:auto;display:block;background-color: #10b2ca; border: none; color: white; padding: 6px 6px; text-align: center; text-decoration: none; font-size: 11px;" type="submit">{{ime}}</button>
                    </form>
                </td>
            </tr>
            % end
            % end
        </table>
    </div>
    
    <div>
        <table id="mreze">
            <tr>
                <th>
                    Rešene mreže:
                </th>
            </tr>
            % for ime, (_, stanje) in sudokually.mreze.items():
            % if stanje == model.RESEN_SUDOKU:
            <tr>
                <td>
                    <form action="/obstojece_mreze/{{ime}}/" method="POST">
                        <button style="margin:auto;display:block;background-color: #10b2ca; border: none; color: white; padding: 6px 6px; text-align: center; text-decoration: none; font-size: 11px;" type="submit">{{ime}}</button>
                    </form>
                </td>
            </tr>
            % end
            % end
        </table>
    </div>
</section>
<br>
<section class="container">
    <form action="/SudokuAlly/" method="get">
        <button style="margin-left:397px" type="submit">DOMOV</button>
    </form>
</section>

% else:
<section class="container">
    <div style="float: left;margin-left:25px;margin-right:33px">
        <table id="mreze">
            <tr>
                <th>
                    Odprte mreže:
                </th>
            </tr>
            % for ime, (_, stanje) in sudokually.mreze.items():
            % if not (stanje == model.RESEN_SUDOKU):
            <tr>
                <td>
                    <form action="/obstojece_mreze/{{ime}}/" method="POST">
                        <button style="margin:auto;display:block;background-color: #10b2ca; border: none; color: white; padding: 6px 6px; text-align: center; text-decoration: none; font-size: 11px;" type="submit">{{ime}}</button>
                    </form>
                </td>
            </tr>
            % end
            % end
        </table>
    </div>
    
    <div>
        <table id="mreze">
            <tr>
                <th>
                    Rešene mreže:
                </th>
            </tr>
            % for ime, (_, stanje) in sudokually.mreze.items():
            % if stanje == model.RESEN_SUDOKU:
            <tr>
                <td>
                    <form action="/obstojece_mreze/{{ime}}/" method="POST">
                        <button style="margin:auto;display:block;background-color: #10b2ca; border: none; color: white; padding: 6px 6px; text-align: center; text-decoration: none; font-size: 11px;" type="submit">{{ime}}</button>
                    </form>
                </td>
            </tr>
            % end
            % end
        </table>
    </div>
</section>
<br>
<section class="container">
    <form action="/SudokuAlly/" method="get">
        <button style="margin-left:135px" type="submit">DOMOV</button>
    </form>
</section>
% end
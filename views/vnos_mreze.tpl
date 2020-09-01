% import model
% rebase('base.tpl')

<style>
    table { border-collapse: collapse; font-family: Calibri, sans-serif; }
    colgroup, tbody { border: solid medium; }
    td { border: solid thin; height: 1.4em; width: 1.4em; text-align: center; padding: 0; }
</style>

<nav class="panel">
    <p class="panel-heading">
        <strong>Vnesi števila med vključno 1 in 9.</strong><br>
        <i>Če števila ni, lahko vneseš 0, ali pa pustiš prazno polje.</i>
    </p>
    <div class="panel-block">
        <form action="/nova_mreza/" method="POST">
            Ime tvoje mreže:
            <input type="text", name="ime", autofocus><br><br>
            <table>
                <!-- colgroup in tbody značke so prisotne zaradi odebeljenih črt v sudoku mreži -->
                % for _ in range(3):
                <colgroup><col><col><col></colgroup>
                % end
                
                % for trovrstje in range(3):
                <tbody>
                    
                    % for vrsta_v_trovrstju in range(3):
                    <tr>
                        
                        % for stolpec in range(9):
                        <td>
                            
                            % vrsta = 3 * trovrstje + vrsta_v_trovrstju
                            <input size="1" type="text", name="{{vrsta}}{{stolpec}}", maxlength="1">
                            
                        </td>
                        % end
                        
                    </tr>
                    % end
                    
                </tbody>
                % end
            </table>
            <br>
            <button type="submit">Ustvari mrežo</button>
            
        </form>
        <br>
        <form action="/SudokuAlly/" method="GET">
            <button type="submit">Zavrzi & Domov</button>
        </form>
    </div>
</nav>
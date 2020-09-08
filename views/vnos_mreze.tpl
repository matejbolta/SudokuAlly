% import model
% rebase('base.tpl')

<style>
    table { border-collapse: collapse; }
    colgroup, tbody { border: solid medium; }
    td { border: solid thin; padding: 0px; }
    strong { color: #f19012; }
    td { height: 34px; width: 34px }
</style>

<br>
<nav>
    <div>
        <div>
            <form action="/SudokuAlly/nova_mreza/" method="POST">
                Ime mreže:<br>
                <input type="text", name="ime", autofocus><br><br>
            </div>
            <strong>
                % if opozorilo == 'noname':
                Ne pozabi vnesti prepoznavnega imena mreže!<br><br>
                % elif opozorilo == 'int':
                Ne vnašaj črk ter drugih znakov!<br><br>
                % elif opozorilo == 'unsolvable':
                Prepričaj se, da je vnesena mreža rešljiva!<br><br>
                % end
            </strong>
            <strong style="color:black">Vnesi števila med vključno 1 in 9.</strong><br><br>
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
                            <input style="height:100%;width:100%;box-sizing:border-box;" type="text", name="{{vrsta}}{{stolpec}}", maxlength="1">
                            
                        </td>
                        % end
                        
                    </tr>
                    % end
                    
                </tbody>
                % end
            </table><br>
            
            <button style="padding-left:12px; padding-right:12px" type="submit">DODAJ MREŽO</button>
        </form>
        
        <form action="/SudokuAlly/brisanje_sledi/" method="POST">
            <button style="margin-top:12px" type="submit">ZAVRZI & DOMOV</button>
        </form>
        
    </div>
</nav>
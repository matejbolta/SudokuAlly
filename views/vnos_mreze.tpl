% import model
% rebase('base.tpl')

<style>
    table { border-collapse: collapse; font-family: Calibri, sans-serif; }
    colgroup, tbody { border: solid medium; }
    td { border: solid thin; padding: 0; }
</style>

<nav style="margin-left:45px" class="panel">
    <div class="panel-block">
        <div class="contentcontainer med left" style="margin-left: 65px;">
            <form action="/nova_mreza/" method="POST">
                <i>Ime mreže:</i>
                <input type="text", name="ime", autofocus><br><br>
            </div>
            % if opozorilo == 'noname':
            <strong style="margin-left:31px;color:#f19012;">Ne pozabi vnesti prepoznavnega imena mreže!</strong><br><br>
            % elif opozorilo == 'int':
            <strong style="margin-left:70px;color:#f19012;">Ne vnašaj črk ter drugih znakov!</strong><br><br>
            % elif opozorilo == 'unsolvable':
            <strong style="margin-left:43px;color:#f19012;">Prepričaj se, da je vnesena mreža rešljiva!</strong><br><br>
            % end
            <strong style="margin-left:70px">Vnesi števila med vključno 1 in 9.</strong><br><br>
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
                        <td style="height:40px;width:40px">
                            
                            % vrsta = 3 * trovrstje + vrsta_v_trovrstju
                            <input style="height:100%;width:100%;box-sizing:border-box;" type="text", name="{{vrsta}}{{stolpec}}", maxlength="1">
                            
                        </td>
                        % end
                        
                    </tr>
                    % end
                    
                </tbody>
                % end
            </table>
            <br>
            <table>
                <tr>
                    <button style="margin-left:137px;" type="submit">DODAJ MREŽO</button>
                </form>
                
                <form action="/brisanje_sledi/" method="POST">
                    <button style="margin-left:18px;" type="submit">ZAVRZI & DOMOV</button>
                </form>
            </tr>
        </table>
        
    </div>
</nav>
% import model
% rebase('base.tpl')
{{stanje}}<br>
<nav style="margin-left:45px" class="panel">
    <div class="panel-block">
        <strong style="color:#46cadf;margin-left:125px">{{ime}}</strong><br><br>

        % if stanje == model.NAPACEN_UGIB:
        <strong style="margin-left:68px;color:#f14612;">Število, ki ste ga vnesli, je napačno.</strong><br><br>
        % elif stanje == model.ZAPOLNJENO_POLJE:
        <strong style="margin-left:112px;color:#f19012;">Izberite prazno polje!</strong><br><br>
        % elif stanje == model.PRAVILEN_UGIB:
        <strong style="margin-left:103px;color:#26d60f;">Vnesli ste pravo število!</strong><br><br>
        % elif stanje == model.NEVELJAVEN_VNOS:
        <strong style="margin-left:53px;color:#f19012;">Vnašajte le števila med vključno 1 in 9!</strong><br><br>
        % elif stanje == model.USPESNA_POMOC:
        <strong style="margin-left:132px;color:#26d60f;">Uspešna pomoč!</strong><br><br>
        % end
        
        <table style="border-collapse: collapse; font-family: Calibri, sans-serif;">
            % for _ in range(3):
            <colgroup style="border:solid medium;"><col><col><col></colgroup>
            % end
            
            % for trovrstje in range(3):
            <tbody style="border:solid medium;">
                
                % for vrsta_v_trovrstju in range(3):
                <tr>
                    
                    % for stolpec in range(9):
                    <td style="padding:0;border:1px solid #ddd;text-align:center;vertical-align:middle;height:40px;width:40px">
                        % vrsta = 3 * trovrstje + vrsta_v_trovrstju
                        % if mreza.tabela[vrsta][stolpec]:
                        {{mreza.tabela[vrsta][stolpec]}}
                        % end
                    </td>
                    % end
                    
                </tr>
                % end
                
            </tbody>
            % end
        </table>
        
    </div>
</nav><br>
<!-- 
    Namesto vsega tega bi lahko preprosto rekli
    <pre>{{mreza}}</pre>
    saj je tudi ta prikaz povsem pregleden.
-->

% if stanje != model.RESEN_SUDOKU:
<nav style="margin-left:50px" class="panel">
    <table>
        <tr>
            <form action="/poskus_namig/vnesi_stevilko/" method="POST">
                <td><i>Vrsta:</i> <input style="height:30px;width:30px;box-sizing:border-box;" size="1" type="text", name="vrsta", maxlength="1"></td>
                <td style="color:white">..</td>
                <td><i>Stolpec:</i> <input style="height:30px;width:30px;box-sizing:border-box;" size="1" type="text", name="stolpec", maxlength="1"></td>
                <td style="color:white">..</td>
                <td><i>Število:</i> <input style="height:30px;width:30px;box-sizing:border-box;" size="1" type="text", name="stevilo", maxlength="1"></td>
                <td style="color:white">aaaa</td>
                <td><button type="submit">VNESI</button></td>
            </form>
        </tr>
        <tr>
            <form action="/poskus_namig/resi_polje/" method="POST">
                <td><i>Vrsta:</i> <input style="height:30px;width:30px;box-sizing:border-box;" size="1" type="text", name="vrsta", maxlength="1"></td>
                <td></td>
                <td><i>Stolpec:</i> <input style="height:30px;width:30px;box-sizing:border-box;" size="1" type="text", name="stolpec", maxlength="1"></td>
                <td></td><td></td><td></td>
                <td style="text-align: right;"> <button type="submit">REŠI</button> </td>
            </form>
        </tr>
    </table>
</nav>

<form action="/poskus_namig/resi_nakljucno/" method="POST">
    <button style="margin-top:16px;margin-left:154px;" type="submit">REŠI NAKLJUČNO POLJE</button>
</form>

<form action="/poskus_namig/resi_vse/" method="POST">
    <button style="margin-top:3px;margin-left:159px;" type="submit">REŠI CELOTNO MREŽO</button>
</form>

<form action="/poskus_namig/izbris_mreze/" method="POST">
    <button style="margin-top:3px;margin-left:182px;" type="submit">IZBRIŠI MREŽO</button>
</form>
% end

<form action="/SudokuAlly/" method="GET">
    <button style="margin-top:3px;margin-left:202px;" type="submit">DOMOV</button>
</form>
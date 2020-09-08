% import model
% rebase('base.tpl')

<style>
    input { 
        height:30px;
        width:30px;
        box-sizing:border-box;
        margin-left:4px;
    }
</style>
<br>
<strong style="color:#50d5e9;font-size:18px;">{{ime}}</strong><br><br>

% if stanje == model.NAPACEN_UGIB:
<strong style="color:#e9b04e">Število, ki ste ga vnesli, je napačno.</strong><br><br>
% elif stanje == model.ZAPOLNJENO_POLJE:
<strong style="color:#e9b04e;">Izberite prazno polje!</strong><br><br>
% elif stanje == model.PRAVILEN_UGIB:
<strong style="color:#2fc96a;">Vnesli ste pravo število!</strong><br><br>
% elif stanje == model.NEVELJAVEN_VNOS:
<strong style="color:#e9b04e;">Vnašajte le števila med vključno 1 in 9!</strong><br><br>
% elif stanje == model.USPESNA_POMOC:
<strong style="color:#2fc96a;">Uspešna pomoč!</strong><br><br>
% end

<table style="border-collapse:collapse;">
    % for _ in range(3):
    <colgroup style="border:solid medium;"><col><col><col></colgroup>
    % end
    
    % for trovrstje in range(3):
    <tbody style="border:solid medium;">
        
        % for vrsta_v_trovrstju in range(3):
        <tr>
            
            % for stolpec in range(9):
            <td style="padding:0px;border:solid thin #ddd;text-align:center;vertical-align:middle;height:34px;width:34px">
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
</table><br>
<!-- 
    Tudi prikaz
    <pre>{{mreza}}</pre>
    je povsem pregleden.
-->

% if stanje != model.RESEN_SUDOKU:
<table>
    <tr>
        <form action="/SudokuAlly/poskus_namig/vnesi_stevilko/" method="POST">
            <td>Vrsta:  <input size="1" type="text", name="vrsta", maxlength="1"></td>
            <td style="color:white">..</td>
            <td>Stolpec:  <input size="1" type="text", name="stolpec", maxlength="1"></td>
            <td style="color:white">..</td>
            <td>Število:  <input size="1" type="text", name="stevilo", maxlength="1"></td>
            <td style="color:white">...........</td>
            <td><button type="submit">VNESI</button></td>
        </form>
    </tr>
    <tr>
        <form action="/SudokuAlly/poskus_namig/resi_polje/" method="POST">
            <td>Vrsta:  <input size="1" type="text", name="vrsta", maxlength="1"></td>
            <td></td>
            <td>Stolpec:  <input size="1" type="text", name="stolpec", maxlength="1"></td>
            <td></td> <td></td> <td></td>
            <td> <button style="padding-left:10px;padding-right:10px" type="submit">REŠI</button> </td>
        </form>
    </tr>
</table>

<table>
    <tr>
        <td>
            <form action="/SudokuAlly/poskus_namig/resi_nakljucno/" method="POST">
                <button style="margin-top:15px;" type="submit">REŠI NAKLJUČNO POLJE</button>
            </form>
        </td>
        <td>
            <form action="/SudokuAlly/poskus_namig/izbris_mreze/" method="POST">
                <button style="margin-top:15px;margin-left:46px;" type="submit">IZBRIŠI MREŽO</button>
            </form>
        </td>
    </tr>
    <tr>
        <td>        
            <form action="/SudokuAlly/poskus_namig/resi_vse/" method="POST">
                <button style="padding-left:14px;padding-right:14px;margin-top:3px;" type="submit">REŠI CELOTNO MREŽO</button>
            </form>
        </td>
        <td>
            <form action="/SudokuAlly/" method="GET">
                <button style="padding-left:23px;padding-right:23px;margin-top:3px;margin-left:46px;" type="submit">DOMOV</button>
            </form>
        </td>
    </tr>
</table>
% end

% if stanje == model.RESEN_SUDOKU:
<form action="/SudokuAlly/poskus_namig/izbris_mreze/" method="POST">
    <button type="submit">IZBRIŠI MREŽO</button>
</form>

<form action="/SudokuAlly/" method="GET">
    <button style="padding-left:23px;padding-right:23px;margin-top:9px;" type="submit">DOMOV</button>
</form>
% end
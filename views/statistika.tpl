% import model
% rebase('base.tpl')

<style>
    table { border-collapse: collapse; width: 500px; }
    
    #statistika td, #statistika th {
        font-size: 18px;
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }
    
    #statistika tr:nth-child(even) { background-color: #f2f2f2; }
    
    #statistika tr:hover { background-color: #ddd; }
    
    #statistika th {
        font-size: 19px;
        padding: 12px;
        background-color: #50d5e9;
        color: white;
        text-align: center;
    }

    button { margin-left:454px; }
</style>

<br><br>

<table id="statistika">
    <tr>
        <th>Kategorija</th>
        <th>Statistični podatek</th>
    </tr>
    <tr>
        <td>
            Število dosedanjih mrež:
        </td>
        <td>
            {{statistike.get('stevilo_mrez', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Število rešenih mrež:
        </td>
        <td>
            {{statistike.get('stevilo_koncanih_mrez', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Delež odprtih mrež:
        </td>
        <td>
            {{statistike.get('odstotek_odprtih_mrez', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Najtežja mreža & njena začetna polja:
        </td>
        <td>
            {{statistike.get('najtezja_mreza', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Skupno število uganjenih polj:
        </td>
        <td>
            {{statistike.get('skupno_stevilo_uganjenih_polj', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Skupni delež izpolnjenih polj:
        </td>
        <td>
            {{statistike.get('povprecje_polnih_polj', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Povprečno število začetnih polj:
        </td>
        <td>
            {{statistike.get('povprecje_polnih_zacetnih_polj', 'N/A')}}
        </td>
    </tr>
</table>

<br>

<form action="/SudokuAlly/" method="get">
    <button type="submit">DOMOV</button>
</form>
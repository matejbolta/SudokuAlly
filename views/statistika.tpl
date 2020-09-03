% import model
% rebase('base.tpl')

<style>
    #statistika {
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 490px;
        margin-left:15px
    }
    
    #statistika td, #statistika th {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center; 
        vertical-align: middle;
    }
    
    #statistika tr:nth-child(even){background-color: #f2f2f2;}
    
    #statistika tr:hover {background-color: #ddd;}
    
    #statistika th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #50d5e9;
        color: white;
        text-align: center; 
        vertical-align: middle;
    }
    button { margin:0px 0px 0px 439px; }
</style>

<br><br>

<table id="statistika">
    <tr>
        <th>Kategorija</th>
        <th>Statistični podatek</th>
    </tr>
    <tr>
        <td>
            <i>Število dosedanjih mrež:</i>
        </td>
        <td>
            {{statistike.get('stevilo_mrez', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            <i>Število rešenih mrež:</i>
        </td>
        <td>
            {{statistike.get('stevilo_koncanih_mrez', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            <i>Delež odprtih mrež:</i>
        </td>
        <td>
            {{statistike.get('odstotek_odprtih_mrez', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            <i>Najtežja mreža & njena začetna polja:</i>
        </td>
        <td>
            {{statistike.get('najtezja_mreza', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            <i>Skupno število uganjenih polj:</i>
        </td>
        <td>
            {{statistike.get('skupno_stevilo_uganjenih_polj', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            <i>Skupni delež izpolnjenih polj:</i>
        </td>
        <td>
            {{statistike.get('povprecje_polnih_polj', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            <i>Povprečno število začetnih polj:</i>
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
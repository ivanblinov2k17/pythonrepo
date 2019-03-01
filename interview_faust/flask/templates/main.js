Vue.component('product',{
    template:`
    <div class="product">
        <table border=2px>
            <tr>
                <th>Имя</th>
                <th>Фамилия</th>
                <th>Дата</th>
                <th>Сумма</th>
            </tr>
            
        </table>
    </div>`
})
var app = new Vue({
    el: '#app'
})
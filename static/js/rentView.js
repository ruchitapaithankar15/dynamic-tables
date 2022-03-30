//Ruchita Paithankar, rhp44@drexel.edu
//CS530: DUI, Assignment 2
function rentView() {

    this.updateRows = (bikes) => {
        $('#table').empty();
            for (let col = 0; col < bikes.length; col++) {
                const data = bikes[col];
                const table = $(`
                <tr id="${data.id}" class="${data.available == 0 ? 'unavailable' : ''}">
                <td><img class="bike-images" src="/static/img/bikes/${data.image}" alt="bike-image"/></td>
                <td>${data.name}</td>
                <td>${data.available}</td>
                <td>
                <a>
                <button  id="minus" class="btn btn-secondary ${data.available == 0 ? 'unclickable' : ''}">- </button>
                <button  id="plus" class="btn btn-secondary">+</button>
                </a>
                </div>
                </td>
                </tr>
                `);
                if (data.available<3){
                $(table).find('#plus').on('click', _ => {
                this.increment(data);

                });}
                if (data.available>0){
                    $(table).find('#minus').on('click', _ => {
                        this.decrement(data);
                       
                        });
                }

                $('#table').append(table);
            }
    
        }


    $(document).find('#Reset').on('click', _ => {
            this.reset();
    });

    this.load = () => {
        $.get('/api/get_bikes',null, (bikes) => {
            this.updateRows(bikes);
        });
    }
    
    //to resent the availability 
    this.reset = () => {
        $.post('/api/reset_bikes', {
            available:3,
        }, (data) => {
            this.updateRows(data);
            });
    }

    //to increment the availability
    this.increment= (bike) => {
        $.post('/api/update_bikes', {

            id: bike.id,
            available: bike.available +1 ,
        }, (bikes) => {
            this.updateRows(bikes);
        });
    }

    //to decrement the availability
    this.decrement= (bike) => {
        $.post('/api/update_bikes', {
                id: bike.id,
            available: bike.available -1  ,
        }, (bikes) => {
            this.updateRows(bikes);
        });
    }


}
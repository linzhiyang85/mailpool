function randomize_pick_email_address_field(){
    document.getElementById("pick_email_address").value = faker.internet.email().split('@')[0];
}

function binding(){
    let elem = null;
    // in mail preview page
    elem = document.getElementById('copy_mail_address_to_clipboard');
    if(elem){
        elem.addEventListener('click', function(evt){
            let text_to_copy = document.getElementById("pick_email_address").value + '@mailpool.xyz';
            navigator.clipboard.writeText(text_to_copy);
            let email_copied_toast = document.getElementById('email_copied');
            new bootstrap.Toast(email_copied_toast).show();
        });
    }

    elem = document.getElementById('pick_for_me');
    if(elem){
        elem.addEventListener('click', function(evt){
            randomize_pick_email_address_field();
        });
    }
    // in mail detail page
    elem = document.getElementById('message-toggle');
    if(elem){
        elem.addEventListener('click', function(evt){
            let status = this.dataset['status'];
            if(status.startsWith('#')){
                expanding_items = document.getElementsByClassName('show');
                if(expanding_items.length > 0){
                    this.dataset['previd'] = expanding_items[0].id;
                }else{
                    this.dataset['previd'] = '';
                }

                // expand all items
                let message_items = document.getElementsByClassName('accordion-item');
                for(let i = 0; i < message_items.length; i++){
                    message_items[i].firstElementChild.getElementsByTagName('button')[0].classList.remove('collapsed');
                    message_items[i].lastElementChild.classList.add('show');
                }
                this.dataset['status'] = 'expanded'
            }else if(status == 'expanded'){
                // collapse all items
                let message_items = document.getElementsByClassName('accordion-item');
                for(let i = 0; i < message_items.length; i++){
                    message_items[i].firstElementChild.getElementsByTagName('button')[0].classList.add('collapsed');
                    message_items[i].lastElementChild.classList.remove('show');
                }
                this.dataset['status'] = 'collapsed'
            }else if(status == 'collapsed'){
                let prev = this.dataset['previd'];
                let message_items = document.getElementsByClassName('accordion-item');
                for(let i = 0; i < message_items.length; i++){
                    if(message_items[i].lastElementChild.id == prev){
                        //expand it
                        message_items[i].firstElementChild.getElementsByTagName('button')[0].classList.remove('collapsed');
                        message_items[i].lastElementChild.classList.add('show');
                    }else{
                        //collapse it
                        message_items[i].firstElementChild.getElementsByTagName('button')[0].classList.add('collapsed');
                        message_items[i].lastElementChild.classList.remove('show');
                    }
                }
                this.dataset['status'] = '#' + prev;
            }
        });
    }
}


document.addEventListener('DOMContentLoaded', function(){
    // do something
    binding();
});

import email
from email import message
from flask import render_template, request
#app.py file ile baglanti qurulur
from app import app
from forms import ContactForm
from models import contact



#flask form ucun yazilan numune
#post_data - web site dan daxil olan melumatlari elde etmek ucundu, sonradan bazaya gondere bilerik
@app.route('/contact', methods=["GET", "POST"])
def contact():
    # GET olduqda datasiz bosh sehife acilir, POST olduqda daxil olan data bize gelir
    #method GET dirse post_data bosh olur
    post_data = request.form # formdan gelen
    print(post_data)
    form = ContactForm() #niye?
    #eger metdo POST dursa ContactForm gonder, sonra validate (yoxla) ele, sonra (form=form) form-u html gonder
    if request.method == 'POST':
        form = ContactForm(data = post_data) 
    # ContactForm(data = post_data) - bu onu gosterir ki sitedan - > request.form -->post_data --> data --> bu ise ContactForm un icine duwur
    # ContactForm ise forms.py icinde uygun datani uygun yere yerleshdirecek
        if form.validate_on_submit():
    #valiadte etdikden sonra gonderir form = form ve sehv yazilmiwlari ekranda goruruk
            Contact = contact(full_name=form.full_name.data, email=form.email.data, message=form.message.data) 
            Contact.save()
            print(Contact)

    return render_template('contact.html', form = form)




# flask model ucun yazilan

# post_list=['Post 1', 'Post 2', 'Post 3', 'Post 4']

# @app.route("/post/<int:post_index>")
# def post_detail(post_index):
#     if post_index < len(post_list)+1:
#         post_choose = post_list[post_index-1]
#         # return "Hello, World!"
#         return render_template("index.html", post=post_choose)
#     else:
#         return "index out of range"


# @app.route("/posts")
# def post_full():
#     return render_template("posts.html", show_block=True, posts=post_list)
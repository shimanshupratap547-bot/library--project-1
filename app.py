from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# किताबों का डेटा स्टोर करने के लिए एक लिस्ट (शुरुआती डेटा के साथ)
books = [
    {"id": 1, "title": "Python Programming", "author": "Guido van Rossum"},
]

# 1. मुख्य पेज - जहाँ किताबें दिखाई देंगी
@app.route('/')
def index():
    return render_template('index.html', books=books)

# 2. नई किताब जोड़ने का रूट (Route)
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    
    if title and author:
        # हर नई किताब के लिए एक नई unique ID बनाना
        new_id = max([b['id'] for b in books]) + 1 if books else 1
        books.append({"id": new_id, "title": title, "author": author})
        
    return redirect('/')

# 3. किताब हटाने (Delete) का रूट (Route)
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    global books
    # उस ID वाली किताब को छोड़कर बाकी सभी किताबों को लिस्ट में रखना
    books = [book for book in books if book['id'] != book_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
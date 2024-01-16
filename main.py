# добавление нужных модулей
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import mydb
import mysql.connector

# Создаем экземпляр приложения Flask и указываем папку с шаблонами
app = Flask(__name__, template_folder='templates')

# Устанавливаем соединение с базой данных, используя конфигурацию mydb
db_conn = mysql.connector.connect(**mydb)

# Определяем маршрут для корневой (главной) страницы приложения
@app.route('/')
def index():
    # создаем курсор
    cursor = db_conn.cursor()

    # Получаем список преподавателей из базы данных
    cursor.execute('SELECT teachers.id, teachers.name, departments.name, gender.name, teachers.date1, zvanie.name, dol.name, teachers.pstag, teachers.ostag, teachers.number, teachers.email, teachers.kolvo1, teachers.kolvo2, '
                   'podraz.name, teachers.namepr, teachers.date2, teachers.date3, teachers.raspis, teachers.kolvo3, teachers.obraz FROM teachers INNER JOIN departments ON teachers.iddepart=departments.id '
                   'INNER JOIN gender ON teachers.gender=gender.id '
                   'INNER JOIN zvanie ON teachers.zvanie=zvanie.id '
                   'INNER JOIN dol ON teachers.dol=dol.id '
                   'INNER JOIN podraz ON teachers.podraz=podraz.id')
    teachers = cursor.fetchall()

    # Получаем список отделов из базы данных
    cursor.execute('SELECT * FROM departments')
    departments = cursor.fetchall()

    # Получаем список банков из базы данных
    cursor.execute('SELECT * FROM bank')
    bank = cursor.fetchall()

    # Получаем список званий из базы данных
    cursor.execute('SELECT * FROM zvanie')
    zvanie = cursor.fetchall()

    # Получаем список программ из базы данных
    cursor.execute('SELECT * FROM programm')
    programm = cursor.fetchall()

    # Получаем список подразделений из базы данных
    cursor.execute('SELECT * FROM podraz')
    podraz = cursor.fetchall()

    cursor.execute('SELECT * FROM listen')
    listen = cursor.fetchall()

    cursor.execute('SELECT * FROM groupp')
    groupp = cursor.fetchall()

    cursor.execute('SELECT * FROM gender')
    gender = cursor.fetchall()

    cursor.execute('SELECT * FROM dol')
    dol = cursor.fetchall()

    cursor.execute('SELECT * FROM list')
    list = cursor.fetchall()
    cursor.close()

    # Возвращает HTML-страницу с использованием шаблона 'index.html' и передает данные на эту страницу

    return render_template('index.html', teachers=teachers, departments=departments, bank=bank, zvanie=zvanie, programm=programm, podraz=podraz, listen=listen, groupp=groupp, gender=gender, dol=dol, list=list)


# Страница добавления преподавателя
@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        date1 = request.form['br']
        pstag = request.form['pstag']
        ostag = request.form['ostag']
        number = request.form['number']
        email = request.form['email']
        kolvo1 = request.form['kolvo1']
        kolvo2 = request.form['kolvo2']
        podraz = request.form['podraz']
        zvanie = request.form['zvanie']
        namepr = request.form['namepr']
        date2 = request.form['date2']
        date3 = request.form['date3']
        raspis = request.form['raspis']
        kolvo3 = request.form['kolvo3']
        obraz = request.form['obraz']
        dol = request.form['dol']
        department_id = request.form['department']
        cursor = db_conn.cursor()

        # Добавляем преподавателя в базу данных
        cursor.execute('INSERT INTO teachers (name, iddepart, gender, date1, zvanie, dol, pstag, ostag, number, email, kolvo1, kolvo2, podraz, namepr, date2, date3, raspis, kolvo3, obraz) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, department_id, gender, date1, zvanie, dol, pstag, ostag, number, email, kolvo1, kolvo2, podraz, namepr, date2, date3, raspis, kolvo3, obraz))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    cursor = db_conn.cursor()

    # Получаем список отделов из базы данных
    cursor.execute('SELECT * FROM departments')
    departments = cursor.fetchall()

    cursor.execute('SELECT * FROM zvanie')
    zvanie = cursor.fetchall()

    cursor.close()
    return render_template('add_teacher.html', departments=departments, zvanie=zvanie)

# Страница добавления списка
@app.route('/add_list', methods=['GET', 'POST'])
def add_list():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender1']
        date1 = request.form['br1']
        osum = request.form['osum']
        sum1 = request.form['sum1']
        sum2 = request.form['sum2']
        postup = request.form['postup']
        ostal = request.form['ostal']
        graz = request.form['graz']
        podraz = request.form['podraz1']
        fioplat = request.form['name1']
        bank = request.form['bank']
        listen = request.form['listen']
        programm = request.form['programm']
        namepr = request.form['namepr1']
        date4 = request.form['date44']
        date3 = request.form['date33']
        raspis = request.form['raspis1']
        kolvo1 = request.form['kolvo11']
        groupp = request.form['groupp']
        date2 = request.form['date22']
        cursor = db_conn.cursor()

        # Добавляем преподавателя в базу данных
        cursor.execute('INSERT INTO list (name, gender, date1, graz, osum, sum1, sum2, postup, ostal, date2, fioplat, bank, podraz, listen, programm, namepr, kolvo1, date3, date4, groupp, raspis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (name, gender, date1, graz, osum, sum1, sum2, postup, ostal, date2, fioplat, bank, podraz, listen, programm, namepr, kolvo1, date3, date4, groupp, raspis))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    cursor = db_conn.cursor()

    # Получаем список отделов из базы данных
    cursor.execute('SELECT * FROM departments')
    departments = cursor.fetchall()

    cursor.execute('SELECT * FROM zvanie')
    zvanie = cursor.fetchall()

    cursor.close()
    return render_template('add_list.html', departments=departments, zvanie=zvanie)


# Страница редактирования преподавателя
@app.route('/edit_teacher/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    cursor = db_conn.cursor()

    # Получаем преподавателя по ID
    cursor.execute('SELECT * FROM teachers WHERE id = %s', (id,))
    teacher = cursor.fetchone()

    if teacher:
        if request.method == 'POST':
            name = request.form['name']
            gender = request.form['gender']
            date1 = request.form['br']
            pstag = request.form['pstag']
            ostag = request.form['ostag']
            number = request.form['number']
            email = request.form['email']
            kolvo1 = request.form['kolvo1']
            kolvo2 = request.form['kolvo2']
            podraz = request.form['podraz']
            zvanie = request.form['zvanie']
            namepr = request.form['namepr']
            date2 = request.form['date2']
            date3 = request.form['date3']
            raspis = request.form['raspis']
            kolvo3 = request.form['kolvo3']
            obraz = request.form['obraz']
            dol = request.form['dol']
            department_id = request.form['department']

            # Обновляем данные преподавателя в базе данных
            cursor.execute('UPDATE teachers SET name = %s, iddepart = %s, gender = %s, date1 = %s, pstag = %s, ostag = %s, number = %s, email = %s, kolvo1 = %s, kolvo2 = %s, podraz = %s, zvanie = %s, namepr = %s, date2 = %s, date3 = %s, raspis = %s, kolvo3 = %s, obraz = %s, dol = %s WHERE id = %s', (name, department_id, gender, date1, pstag, ostag, number, email, kolvo1, kolvo2, podraz, zvanie, namepr, date2, date3, raspis, kolvo3, obraz, dol, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        # Получаем список отделов из базы данных
        cursor.execute('SELECT * FROM departments')
        departments = cursor.fetchall()

        cursor.execute('SELECT * FROM gender')
        gender = cursor.fetchall()

        cursor.execute('SELECT * FROM zvanie')
        zvanie = cursor.fetchall()

        cursor.execute('SELECT * FROM dol')
        dol = cursor.fetchall()

        cursor.execute('SELECT * FROM podraz')
        podraz = cursor.fetchall()
        cursor.close()

        return render_template('edit_teacher.html', teacher=teacher, departments=departments, gender=gender, zvanie=zvanie, dol=dol, podraz=podraz)
    else:
        flash('Teacher not found', 'error')
        return redirect(url_for('index'))

# страница редактирования списка
@app.route('/edit_list/<int:id>', methods=['GET', 'POST'])
def edit_list(id):
    cursor = db_conn.cursor()

    # Получаем преподавателя по ID
    cursor.execute('SELECT * FROM list WHERE id = %s', (id,))
    list = cursor.fetchone()

    if list:
        if request.method == 'POST':
            name = request.form['name']
            gender = request.form['gender']
            date1 = request.form['br']
            pstag = request.form['pstag']
            ostag = request.form['ostag']
            number = request.form['number']
            email = request.form['email']
            kolvo1 = request.form['kolvo1']
            kolvo2 = request.form['kolvo2']
            podraz = request.form['podraz']
            zvanie = request.form['zvanie']
            namepr = request.form['namepr']
            date2 = request.form['date2']
            date3 = request.form['date3']
            raspis = request.form['raspis']
            kolvo3 = request.form['kolvo3']
            obraz = request.form['obraz']
            dol = request.form['dol']
            department_id = request.form['department']

            # Обновляем данные преподавателя в базе данных
            cursor.execute('UPDATE list SET name = %s, iddepart = %s, gender = %s, date1 = %s, pstag = %s, ostag = %s, number = %s, email = %s, kolvo1 = %s, kolvo2 = %s, podraz = %s, zvanie = %s, namepr = %s, date2 = %s, date3 = %s, raspis = %s, kolvo3 = %s, obraz = %s, dol = %s WHERE id = %s', (name, department_id, gender, date1, pstag, ostag, number, email, kolvo1, kolvo2, podraz, zvanie, namepr, date2, date3, raspis, kolvo3, obraz, dol, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        # Получаем список отделов из базы данных
        cursor.execute('SELECT * FROM departments')
        departments = cursor.fetchall()

        cursor.execute('SELECT * FROM gender')
        gender = cursor.fetchall()

        cursor.execute('SELECT * FROM zvanie')
        zvanie = cursor.fetchall()

        cursor.execute('SELECT * FROM dol')
        dol = cursor.fetchall()

        cursor.execute('SELECT * FROM podraz')
        podraz = cursor.fetchall()
        cursor.close()

        return render_template('edit_teacher.html', departments=departments, gender=gender, zvanie=zvanie, dol=dol, podraz=podraz)
    else:
        return redirect(url_for('index'))


# Страница удаления преподавателя
@app.route('/delete_teacher/<int:id>', methods=['GET', 'POST'])
def delete_teacher(id):
    cursor = db_conn.cursor()

    # Получаем преподавателя по ID
    cursor.execute('SELECT * FROM teachers WHERE id = %s', (id,))
    teacher = cursor.fetchone()

    if teacher:
        if request.method == 'POST':
            # Удаляем преподавателя из базы данных
            cursor.execute('DELETE FROM teachers WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_teacher.html', teacher=teacher)
    else:
        flash('Teacher not found', 'error')
        return redirect(url_for('index'))


# Страница добавления отдела
@app.route('/add_department', methods=['GET', 'POST'])
def add_department():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO departments (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_department.html')

# страница добавления пола
@app.route('/add_gender', methods=['GET', 'POST'])
def add_gender():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO gender (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_gender.html')

# страница добавления должности
@app.route('/add_dol', methods=['GET', 'POST'])
def add_dol():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO dol (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_dol.html')

# страница добавления группы
@app.route('/add_groupp', methods=['GET', 'POST'])
def add_groupp():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем группу в базу данных
        cursor.execute('INSERT INTO groupp (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_groupp.html')

# страница добавления слушателя
@app.route('/add_listen', methods=['GET', 'POST'])
def add_listen():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO listen (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_listen.html')

# страница добавления подразделения
@app.route('/add_podraz', methods=['GET', 'POST'])
def add_podraz():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO podraz (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_podraz.html')

# страница добавления программы
@app.route('/add_programm', methods=['GET', 'POST'])
def add_programm():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO programm (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_programm.html')

# страница добавления звания
@app.route('/add_zvanie', methods=['GET', 'POST'])
def add_zvanie():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO zvanie (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_zvanie.html')

# страница добавления банка
@app.route('/add_bank', methods=['GET', 'POST'])
def add_bank():
    if request.method == 'POST':
        name = request.form['name']
        cursor = db_conn.cursor()

        # Добавляем отдел в базу данных
        cursor.execute('INSERT INTO bank (name) VALUES (%s)', (name,))
        db_conn.commit()

        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_bank.html')


# Страница редактирования отдела
@app.route('/edit_department/<int:id>', methods=['GET', 'POST'])
def edit_department(id):
    cursor = db_conn.cursor()

    # Получаем отдел по ID
    cursor.execute('SELECT * FROM departments WHERE id = %s', (id,))
    department = cursor.fetchone()

    if department:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные отдела в базе данных
            cursor.execute('UPDATE departments SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_department.html', department=department)
    else:
        return redirect(url_for('index'))

# Страница редактирования слушателя
@app.route('/edit_listen/<int:id>', methods=['GET', 'POST'])
def edit_listen(id):
    cursor = db_conn.cursor()

    # Получаем отдел по ID
    cursor.execute('SELECT * FROM listen WHERE id = %s', (id,))
    listen = cursor.fetchone()

    if listen:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные слушателя в базе данных
            cursor.execute('UPDATE listen SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_listen.html', listen=listen)
    else:
        return redirect(url_for('index'))

# Страница редактирования программы
@app.route('/edit_programm/<int:id>', methods=['GET', 'POST'])
def edit_programm(id):
    cursor = db_conn.cursor()

    # Получаем отдел по ID
    cursor.execute('SELECT * FROM programm WHERE id = %s', (id,))
    programm = cursor.fetchone()

    if programm:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные программы в базе данных
            cursor.execute('UPDATE programm SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_programm.html', programm=programm)
    else:
        return redirect(url_for('index'))

# Страница редактирования звания
@app.route('/edit_zvanie/<int:id>', methods=['GET', 'POST'])
def edit_zvanie(id):
    cursor = db_conn.cursor()

    # Получаем отдел по ID
    cursor.execute('SELECT * FROM zvanie WHERE id = %s', (id,))
    zvanie = cursor.fetchone()

    if zvanie:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные звания в базе данных
            cursor.execute('UPDATE zvanie SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_zvanie.html', zvanie=zvanie)
    else:
        return redirect(url_for('index'))

# Страница редактирования банка
@app.route('/edit_bank/<int:id>', methods=['GET', 'POST'])
def edit_bank(id):
    cursor = db_conn.cursor()

    # Получаем банк по ID
    cursor.execute('SELECT * FROM bank WHERE id = %s', (id,))
    bank = cursor.fetchone()

    if bank:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные банка в базе данных
            cursor.execute('UPDATE bank SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_bank.html', bank=bank)
    else:
        return redirect(url_for('index'))

# Страница редактирования пола
@app.route('/edit_gender/<int:id>', methods=['GET', 'POST'])
def edit_gender(id):
    cursor = db_conn.cursor()

    # Получаем пол по ID
    cursor.execute('SELECT * FROM gender WHERE id = %s', (id,))
    gender = cursor.fetchone()

    if gender:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные пола в базе данных
            cursor.execute('UPDATE gender SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_gender.html', gender=gender)
    else:
        return redirect(url_for('index'))

# Страница редактирования группы
@app.route('/edit_groupp/<int:id>', methods=['GET', 'POST'])
def edit_groupp(id):
    cursor = db_conn.cursor()

    # Получаем группы по ID
    cursor.execute('SELECT * FROM groupp WHERE id = %s', (id,))
    groupp = cursor.fetchone()

    if groupp:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные группы в базе данных
            cursor.execute('UPDATE groupp SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_groupp.html', groupp=groupp)
    else:
        return redirect(url_for('index'))

# Страница редактирования должности
@app.route('/edit_dol/<int:id>', methods=['GET', 'POST'])
def edit_dol(id):
    cursor = db_conn.cursor()

    # Получаем должность по ID
    cursor.execute('SELECT * FROM dol WHERE id = %s', (id,))
    dol = cursor.fetchone()

    if dol:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные должности в базе данных
            cursor.execute('UPDATE dol SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_dol.html', dol=dol)
    else:
        return redirect(url_for('index'))

# Страница редактирования подразделения
@app.route('/edit_podraz/<int:id>', methods=['GET', 'POST'])
def edit_podraz(id):
    cursor = db_conn.cursor()

    # Получаем подразделение по ID
    cursor.execute('SELECT * FROM podraz WHERE id = %s', (id,))
    podraz = cursor.fetchone()

    if podraz:
        if request.method == 'POST':
            name = request.form['name']

            # Обновляем данные подразделения в базе данных
            cursor.execute('UPDATE podraz SET name = %s WHERE id = %s', (name, id))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('edit_podraz.html', podraz=podraz)
    else:
        return redirect(url_for('index'))

# Страница удаления отдела
@app.route('/delete_department/<int:id>', methods=['GET', 'POST'])
def delete_department(id):
    cursor = db_conn.cursor()

    # Получаем отдел по ID
    cursor.execute('SELECT * FROM departments WHERE id = %s', (id,))
    department = cursor.fetchone()

    if department:
        if request.method == 'POST':
            # Удаляем отдел из базы данных
            cursor.execute('DELETE FROM departments WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_department.html', department=department)
    else:
        return redirect(url_for('index'))

# Страница удаления группы
@app.route('/delete_groupp/<int:id>', methods=['GET', 'POST'])
def delete_groupp(id):
    cursor = db_conn.cursor()

    # Получаем группу по ID
    cursor.execute('SELECT * FROM groupp WHERE id = %s', (id,))
    groupp = cursor.fetchone()

    if groupp:
        if request.method == 'POST':
            # Удаляем группу из базы данных
            cursor.execute('DELETE FROM groupp WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_groupp.html', groupp=groupp)
    else:
        return redirect(url_for('index'))

# Страница удаления слушателя
@app.route('/delete_listen/<int:id>', methods=['GET', 'POST'])
def delete_listen(id):
    cursor = db_conn.cursor()

    # Получаем слушателя по ID
    cursor.execute('SELECT * FROM listen WHERE id = %s', (id,))
    listen = cursor.fetchone()

    if listen:
        if request.method == 'POST':
            # Удаляем слушателя из базы данных
            cursor.execute('DELETE FROM listen WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_listen.html', listen=listen)
    else:
        return redirect(url_for('index'))

# Страница удаления подразделения
@app.route('/delete_podraz/<int:id>', methods=['GET', 'POST'])
def delete_podraz(id):
    cursor = db_conn.cursor()

    # Получаем подразделение по ID
    cursor.execute('SELECT * FROM podraz WHERE id = %s', (id,))
    podraz = cursor.fetchone()

    if podraz:
        if request.method == 'POST':
            # Удаляем подразделение из базы данных
            cursor.execute('DELETE FROM podraz WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_podraz.html', podraz=podraz)
    else:
        return redirect(url_for('index'))

# Страница удаления пола
@app.route('/delete_gender/<int:id>', methods=['GET', 'POST'])
def delete_gender(id):
    cursor = db_conn.cursor()

    # Получаем пол по ID
    cursor.execute('SELECT * FROM gender WHERE id = %s', (id,))
    gender = cursor.fetchone()

    if gender:
        if request.method == 'POST':
            # Удаляем пол из базы данных
            cursor.execute('DELETE FROM gender WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_gender.html', gender=gender)
    else:
        return redirect(url_for('index'))

# Страница удаления должности
@app.route('/delete_dol/<int:id>', methods=['GET', 'POST'])
def delete_dol(id):
    cursor = db_conn.cursor()

    # Получаем должность по ID
    cursor.execute('SELECT * FROM dol WHERE id = %s', (id,))
    dol = cursor.fetchone()

    if dol:
        if request.method == 'POST':
            # Удаляем должность из базы данных
            cursor.execute('DELETE FROM dol WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_dol.html', dol=dol)
    else:
        return redirect(url_for('index'))

# Страница удаления программы
@app.route('/delete_programm/<int:id>', methods=['GET', 'POST'])
def delete_programm(id):
    cursor = db_conn.cursor()

    # Получаем программу по ID
    cursor.execute('SELECT * FROM programm WHERE id = %s', (id,))
    programm = cursor.fetchone()

    if programm:
        if request.method == 'POST':
            # Удаляем программу из базы данных
            cursor.execute('DELETE FROM programm WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_programm.html', programm=programm)
    else:
        return redirect(url_for('index'))

# Страница удаления звания
@app.route('/delete_zvanie/<int:id>', methods=['GET', 'POST'])
def delete_zvanie(id):
    cursor = db_conn.cursor()

    # Получаем звание по ID
    cursor.execute('SELECT * FROM zvanie WHERE id = %s', (id,))
    zvanie = cursor.fetchone()

    if zvanie:
        if request.method == 'POST':
            # Удаляем звание из базы данных
            cursor.execute('DELETE FROM zvanie WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_zvanie.html', zvanie=zvanie)
    else:
        return redirect(url_for('index'))

# Страница удаления банка
@app.route('/delete_bank/<int:id>', methods=['GET', 'POST'])
def delete_bank(id):
    cursor = db_conn.cursor()

    # Получаем банк по ID
    cursor.execute('SELECT * FROM bank WHERE id = %s', (id,))
    bank = cursor.fetchone()

    if bank:
        if request.method == 'POST':
            # Удаляем банк из базы данных
            cursor.execute('DELETE FROM bank WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_bank.html', bank=bank)
    else:
        return redirect(url_for('index'))

# Страница удаления списка
@app.route('/delete_list/<int:id>', methods=['GET', 'POST'])
def delete_list(id):
    cursor = db_conn.cursor()

    # Получаем список по ID
    cursor.execute('SELECT * FROM list WHERE id = %s', (id,))
    list = cursor.fetchone()

    if list:
        if request.method == 'POST':
            # Удаляем список из базы данных
            cursor.execute('DELETE FROM list WHERE id = %s', (id,))
            db_conn.commit()

            cursor.close()

            return redirect(url_for('index'))

        cursor.close()

        return render_template('delete_list.html', list=list)
    else:
        return redirect(url_for('index'))

# запуск программы
if __name__ == '__main__':
    app.run(debug=True)
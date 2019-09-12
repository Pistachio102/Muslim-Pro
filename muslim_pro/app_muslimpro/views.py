from django.db import connection
from django.shortcuts import render


# Create your views here.

def sql_select(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    list = []
    i = 0
    for row in results:
        dict = {}
        field = 0
        while True:
            try:
                dict[cursor.description[field][0]] = str(results[i][field])
                field = field + 1
            except IndexError as e:
                break
        i = i + 1
        list.append(dict)
    return list



def index(request):
    if request.method == 'POST':
        sql_string = request.POST.get('sql_string')
        print(sql_string)
        result_list = sql_select(sql_string)
        return render(request, "app_muslimpro/query.html", {'results': result_list})
    return render(request,'app_muslimpro/index.html')



# Create your views here.
# def index(request):
  #  return render(request,'app_muslimpro/index.html')


def any_sql(request,sql_string):
    result_list = sql_select(sql_string)
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html',context)



# complex queries

def show_sura(request, sura_name, language):
    result_list1 = sql_select('SELECT name, english_name, meaning, type FROM sura WHERE english_name=\''+sura_name+'\'')
    result_list2 = sql_select(
        'SELECT Ayah.AyahID, Ayah.AyahText, Ayah.Pronunciation, Translation.Translated_Text FROM Ayah,Translation WHERE Ayah.SuraID = (SELECT SuraID FROM Sura WHERE English_Name =\'' + sura_name + '\')AND '
                                                                                                                                                                                                     'Translation.SuraID = Ayah.SuraID and Translation.AyahID = Ayah.AyahID and translation.languageid =\'' + language + '\'')
    context = {'results': result_list1,
               'results2': result_list2}
    return render(request, 'app_muslimpro/dualQuery.html', context)


def show_nearby_places(request, type):
    result_list = sql_select('SELECT Place.Name FROM Place,UserTable,UserGoesToPlaces WHERE UserTable.UserID=UserGoesToPlaces.UserId AND UserGoesToPlaces.Longitude=Place.Longitude AND '
                             'UserGoesToPlaces.Latitude=Place.Latitude AND UserTable.UserID=1 AND Place.Type=\''+type+'\' AND ((abs(UserTable.Latitude-Place.Latitude)<=1.5 OR abs(Place.Latitude-UserTable.Latitude)<=1.5) '
                             'AND (abs(UserTable.Longitude-Place.Longitude )<=1.5 OR abs(Place.Longitude-UserTable.Longitude )<=1.5))')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)





# simple queries

def names_of_Allah(request):
    result_list = sql_select('SELECT NameID,Arabic,Pronunciation,Translation FROM NamesOfAllah;')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def namaj_tracker(request, user_id):
    result_list = sql_select('SELECT dDate,Fazr,Juhr,Asr,Magrib,Isha FROM DailyEventTracker WHERE UserID='+str(user_id))
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def fast_tracker(request, user_id):
    result_list = sql_select('SELECT dDate,DidFastOrNot FROM DailyEventTracker WHERE UserID='+str(user_id))
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def show_sura_list(request):
    result_list = sql_select('SELECT SuraID,Name,English_Name,Meaning FROM Sura;')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def show_sura_of_particular_type(request, type):
    result_list = sql_select('SELECT SuraID,Name,English_Name,Meaning FROM Sura WHERE Type=\''+type+'\'')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def show_popular_suras(request):
    result_list = sql_select('SELECT SuraID,Name,English_Name,Meaning FROM Sura WHERE Popular_Or_Not=TRUE;')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def show_juz(request, juz_id, language):
    if juz_id == 30:
        result_list = sql_select('SELECT Ayah.* , translation.translated_text FROM Ayah , translation '
                                 'where (((ayah.suraid = (SELECT suraid FROM juz WHERE juzid ='+str(juz_id)+') AND ayah.ayahid >=(SELECT ayahid from juz where juzid ='+str(juz_id)+')) or '
                                 '(ayah.suraid > (SELECT suraid FROM juz WHERE juzid ='+str(juz_id)+')))and ayah.suraid = translation.suraid and ayah.ayahid = translation.ayahid and translation.languageid = \''+language+'\')ORDER BY (ayah.suraid, ayah.ayahid);')
        context = {'results': result_list}
        return render(request, 'app_muslimpro/query.html', context)
    result_list = sql_select('SELECT Ayah.* , translation.translated_text FROM Ayah , translation '
                             'where (((ayah.suraid = (SELECT suraid FROM juz WHERE juzid ='+str(juz_id)+') AND ayah.ayahid >=(SELECT ayahid from juz where juzid ='+str(juz_id)+')) or '
                             '(ayah.suraid > (SELECT suraid FROM juz WHERE juzid ='+str(juz_id)+') and ayah.suraid < (SELECT suraid FROM juz WHERE juzid ='+str(juz_id+1)+')) or '
                             '(ayah.suraid = (SELECT suraid from juz where juzid ='+str(juz_id+1)+') AND ayah.ayahid < (select ayahid from juz where juzid ='+str(juz_id+1)+'))) ) '
                             'and ayah.suraid = translation.suraid and ayah.ayahid = translation.ayahid and translation.languageid = \''+language+'\'ORDER BY (ayah.suraid, ayah.ayahid);')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def next_namaj(request):
    result_list = sql_select('SELECT NamajTime();')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def show_dua(request, category, name, type, language):
    if type=='Ayah':
        result_list = sql_select('SELECT ayah.*, translation.translated_text FROM Dua,ayah,dua_ayah_relation,translation '
                                 'WHERE dua.DuaID = dua_ayah_relation.DuaID AND dua_ayah_relation.SuraID = ayah.SuraID '
                                 'AND dua_ayah_relation.AyahID = ayah.AyahID '
                                 'AND dua.category = \''+category+'\' AND dua.dua_name = \''+name+'\' AND dua.dua_type = \'Ayah\' AND translation.suraid = ayah.suraid '
                                                                                                  'AND translation.ayahid = ayah.ayahid AND translation.languageid = \''+language+'\' AND translation.name_of_translator = \'Muhiuddin Khan\';')
        context = {'results': result_list}
        return render(request, 'app_muslimpro/query.html', context)
    else:
        result_list = sql_select('SELECT hadithverse.* FROM Dua,HadithVerse, dua_hadith_relation WHERE dua.DuaID = dua_hadith_relation.DuaID AND dua_hadith_relation.HadithID = HadithVerse.HadithID AND dua.category = \''+category+'\' AND dua.dua_name = \''+name+'\'AND dua.dua_type = \'Hadith\';')
        context = {'results': result_list}
        return render(request, 'app_muslimpro/query.html', context)


def show_suras_starting_with(request, s_letter):
    result_list = sql_select('SELECT * FROM sura WHERE Sura.english_name LIKE \''+s_letter+'%\' ORDER BY suraid ASC;')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def any_nearby_place(request, user_id):
    result_list = sql_select('SELECT Place.Name,place.type FROM Place, UserTable, UserGoesToPlaces '
                             'WHERE UserTable.UserID = UserGoesToPlaces.UserId AND UserGoesToPlaces.Longitude = Place.Longitude '
                             'AND UserGoesToPlaces.Latitude = Place.Latitude AND UserTable.UserID ='+str(user_id)+'AND ((abs(UserTable.Latitude - Place.Latitude) <= 10 OR abs(Place.Latitude - UserTable.Latitude) <= 10) AND '
                             '(abs(UserTable.Longitude - Place.Longitude) <= 10 OR abs(Place.Longitude - UserTable.Longitude) <= 10));')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)


def show_quotes(request, id):
    result_list = sql_select('SELECT wallpaper.arabic, wallpaper.translation FROM wallpaper WHERE wallpaperid='+str(id)+';')
    context = {'results': result_list}
    return render(request, 'app_muslimpro/query.html', context)

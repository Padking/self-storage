from box.models import Storage

from django.shortcuts import render

import folium


def prepare_storage_object_info_html(storage_object):
    box_rent_button = '<a href="#">Арендовать бокс</a>' if storage_object.count_free_boxes() > 0 else '<p><b>Все боксы заняты, выберите другой склад.</b></p>'
    storage_object_info_html = """
        <h3>{storage_name}:</h3>
        <p>{address}</p>
        <p>{phone_number}</p>
        <p>Аренда боксов от <b>{min_box_price} руб.</b> в мес.</p>
        <p>{free_squares_meters_count} из {squares_meters_count} м² склада свободно</p>
        <p>{free_boxes_count} из {boxes_count} боксов свободно</p>
        {box_rent_button}
        """.format(
            storage_name=storage_object.alias,
            address=storage_object.address,
            phone_number=storage_object.phone,
            min_box_price=storage_object.count_min_box_price(),
            squares_meters_count=storage_object.count_squares_meters(),
            free_squares_meters_count=storage_object.count_free_squares_meters(),
            boxes_count=storage_object.boxes.count(),
            free_boxes_count=storage_object.count_free_boxes(),
            box_rent_button=box_rent_button
        )

    return storage_object_info_html


def add_storage(folium_map, lat, lon, name, storage_object_info_html, image_url):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(80, 80),
    )

    popup_html = storage_object_info_html.encode('ascii', errors='xmlcharrefreplace').decode('utf-8')

    folium.Marker(
        [lat, lon],
        tooltip=name.encode('ascii', errors='xmlcharrefreplace').decode('utf-8'),
        icon=icon,
        popup=popup_html
    ).add_to(folium_map)


def create_map():
    city_centre = [51.672, 39.1843] # Voronezh centre

    folium_map = folium.Map(location=city_centre, zoom_start=12)

    storages = Storage.objects.all()
    for storage in storages:
        add_storage(
            folium_map,
            storage.latitude,
            storage.longitude,
            storage.alias,
            prepare_storage_object_info_html(storage),
            'https://www.gruzchiki-kiev.net/wp-content/uploads/2021/02/skklad.png'
        )

    return folium_map


def index(request):
    folium_map = create_map()

    return render(request, 'index.html', context={
        'map': folium_map._repr_html_()
    })

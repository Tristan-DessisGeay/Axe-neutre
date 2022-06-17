import element_controller as ec
import geometry_controller as gc
import visualization_controller as vc

elements_ids=ec.get_user_element_ids()

for element_id in elements_ids:
    p1=gc.get_p1(element_id)
    p2=gc.get_p2(element_id)

    line_id=ec.create_line_points(p1,p2)

    couleur_element=vc.get_color(element_id)

    vc.set_color([line_id], couleur_element)
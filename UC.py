from dataclasses import dataclass


# -----------------------------------------------------------------------------
# Q1

# chair 4 parts A,B,C,D
# list of parts and i want to return an output which how chairs

class ManufactureChairs:
    __chair_parts_hash_map = {}

    def insert_part(self, part: str):
        if self.__chair_parts_hash_map.__contains__(part):
            self.__chair_parts_hash_map[part] += 1
        else:
            self.__chair_parts_hash_map[part] = 1

    def chairs_count(self) -> int:
        return min(self.__chair_parts_hash_map.values())

    # def __count_complete_chairs(part_list: list[str]) -> int:
    #     # part counters
    #     a = b = c = d = 0
    #     for part in part_list:
    #         if part == "A":
    #             a += 1
    #         elif part == "B":
    #             b += 1
    #         elif part == "C":
    #             c += 1
    #         else:
    #             d += 1
    #     return min([a, b, c, d])


chairs_obj = ManufactureChairs()
# Enter N number of parts and it will handle it
chairs_obj.insert_part("A")
chairs_obj.insert_part("B")
chairs_obj.insert_part("C")
chairs_obj.insert_part("D")
chairs_obj.insert_part("A")
chairs_obj.insert_part("B")
chairs_obj.insert_part("C")
chairs_obj.insert_part("D")
chairs_obj.insert_part("A")

print(chairs_obj.chairs_count())


# ------------------------------------------------------------------------------------------
# Q2

@dataclass
class StarInfo:
    id: int
    x_coordinate: float
    y_coordinate: float
    wavelength_info: list[int]


# StarInfo(1, 12, 13, [1, 2, 3])


class StarMapper:
    __radio_array = []
    __x_ray_array = []
    __mapped_array: list[tuple[StarInfo, StarInfo]] = []
    __threshold: float = 0

    def __init__(self, x_ray: list[StarInfo], radio: list[StarInfo], threshold: float):
        self.__radio_array = radio
        self.__x_ray_array = x_ray
        self.__threshold = threshold
        self.__map_stars()

    def __map_stars(self):
        for star_r in self.__radio_array:
            for star_x in self.__x_ray_array:
                if pow(star_x.x_coordinate - star_r.x_coordinate, 2) + pow(star_x.y_coordinate - star_r.y_coordinate,
                                                                           2) <= self.__threshold:
                    self.__mapped_array.append((star_x, star_r))

    def get_mapped_stars(self):
        return self.__mapped_array


x_ray_stars = [StarInfo(1, 0, 1, [1, 2, 3]), StarInfo(2, 12, 13, [1, 2, 3]), StarInfo(3, 21, 21, [1, 2, 3]),
               StarInfo(4, 45, 1, [1, 2, 3]), StarInfo(5, 100, 87, [1, 2, 3])]
radio_stars = [StarInfo(11, 1, 1, [1, 2, 3]), StarInfo(12, 12.5, 13.5, [1, 2, 3]), StarInfo(13, 21.9, 21.2, [1, 2, 3]),
               StarInfo(14, 45.21, 1.1, [1, 2, 3]), StarInfo(15, 100.34, 88, [1, 2, 3])]
star_mapper = StarMapper(x_ray=x_ray_stars, radio=radio_stars, threshold=3.0)
mapped = star_mapper.get_mapped_stars()
for x_ray, radio in mapped:
    print(f'XRAY -> {x_ray}')
    print(f'RADIO-> {radio}')
    print("------------------------------------------------------------------")


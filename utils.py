class drawInfo:
    def __init__(self):
        return 
    
    color_dict   = {}
    order_dict   = {}
    legend_names = {}

    __draw_i = 0

    def __setDict(self, gds_layer, color, draw_order, legend_name):
        if not isinstance(gds_layer, int):
            raise Exception("All GDS layers must be integers.")
        if not isinstance(draw_order, int):
            raise Exception("All draw orders must be integers.")

        self.color_dict[gds_layer] = color
        self.order_dict[gds_layer] = draw_order

        if legend_name is not None:
            self.legend_names[gds_layer] = legend_name

    def addLayer(self, gds_layer, color, legend_name=None, draw_order=None):
        # if gds_layer is a list, iterate through the layers and set the color, and draw order to each one
        # create only 1 legend entry to the last gds layer if applicable
        if draw_order is None:
            draw_order = self.__draw_i
            self.__draw_i += 1

        if isinstance(gds_layer, list):
            for idx, l in enumerate(gds_layer):
                if idx >= len(gds_layer) - 1:
                    self.__setDict(l, color, draw_order, legend_name=None)
                else:
                    self.__setDict(l, color, draw_order, legend_name)
        else:
            self.__setDict(gds_layer, color, draw_order, legend_name)

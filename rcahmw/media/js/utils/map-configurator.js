define(['mapbox-gl'], function(MapboxGl){

    let mapConfigurator = {

        preConfig: function(map) {
            const defaultMaxZoom = map.getMaxZoom();
            map.once('render', () => {
                map.setMaxZoom(defaultMaxZoom);
            });
            map.setMaxZoom(17);
            map.addControl(new MapboxGl.ScaleControl({ maxWidth: 200}));
        },
        postConfig: function(map) {
        },
    };

    return mapConfigurator;
});

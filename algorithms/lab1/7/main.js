function hilbertDemo() {

    var svg = d3.select('svg#hilbert-chart'),
        canvasWidth = Math.min(window.innerWidth, window.innerHeight - 100),
        hilbert,
        order = 3;

    function d3Digest() {
        var hilbertData = {
            start: 0,
            length: Math.pow(4, order)
        };

        hilbert.order(order).layout(hilbertData);

        svg.selectAll('path')
            .datum(hilbertData)
            .attr('d', function(d) { return getHilbertPath(d.pathVertices); })
            .attr('transform', function(d) {
                return 'scale('+ d.cellWidth + ') '
                    + 'translate(' + (d.startCell[0] +.5) + ',' + (d.startCell[1] +.5) + ')';
            });

        svg.select('path:not(.skeleton)')
            .transition().duration(order * 1000).ease(d3.easePoly)
            .attrTween('stroke-dasharray', tweenDash);

        function getHilbertPath(vertices) {
            var path = 'M0 0L0 0';

            vertices.forEach(function(vert) {
                switch(vert) {
                    case 'U': path += 'v-1'; break;
                    case 'D': path += 'v1'; break;
                    case 'L': path += 'h-1'; break;
                    case 'R': path += 'h1'; break;
                }
            });
            return path;
        }

       function tweenDash() {
            var l = this.getTotalLength(),
                i = d3.interpolateString("0," + l, l + "," + l);
            return function(t) { return i(t); };
        }
    }

    function orderChange(newOrder) {
        order = newOrder;
        d3Digest();
    }

    function init() {

        hilbert = d3.hilbert()
            .order(order)
            .canvasWidth(canvasWidth)
            .simplifyCurves(false);

        svg.attr("width", canvasWidth).attr("height", canvasWidth);

        var canvas = svg.append('g');
        canvas.append('path').attr('class', 'skeleton');
        canvas.append('path');


        // Order slider
        $('input#hilbert-order').slider({
            step: 1,
            max: 9,
            min: 0,
            value: order,
            tooltip: 'always',
            tooltip_position: 'bottom',
            formatter: function(d) {
                return 'Order: ' + d;
            }
        }).on('change', function(e) {
            orderChange(e.value.newValue);
        });

        d3Digest();
    }

    init();
}

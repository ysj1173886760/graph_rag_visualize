import { BaseNode, Graph} from '@antv/g6';
import { register, ExtensionCategory } from '@antv/g6';

import graph_data from './graph_data.json'

const data = {
  nodes: [
    { id: 'node1', style: { x: 150, y: 100 } },
    { id: 'node2', style: { x: 250, y: 200 } },
    { id: 'node3', style: { x: 450, y: 200 } },
  ],
  edges: [
    { source: 'node1', target: 'node2' },
    { source: 'node1', target: 'node3' },
    { source: 'node2', target: 'node3' },
  ],
};

const graph = new Graph({
  container: 'container',
  data: graph_data,
  node: {
    style: {
      labelPlacement: 'center',
      labelText: (d) => d.id,
      labelWordWrap: true, // enable label ellipsis
      labelFontSize: 1,
      labelMaxWidth: '90%',
      labelBackgroundFill: '#eee',
      labelBackgroundFillOpacity: 0.5,
      labelBackgroundRadius: 2,
      size: 10
    },
  },
  edge: {
    style: {
      labelOffsetY: -4,
      labelTextBaseline: 'bottom',
      // labelText: (d) => d.id,
      labelFontSize: 12,
      labelWordWrap: true,
      labelMaxWidth: '80%',
      labelBackgroundFill: 'red',
      labelBackgroundFillOpacity: 0.5,
      labelBackgroundRadius: 2,
    },
  },
  layout: {
    type: 'force-atlas2',
  },
  behaviors: ['drag-canvas', 'zoom-canvas', 'drag-element'],
});

graph.render();

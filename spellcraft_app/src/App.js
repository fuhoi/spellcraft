import React, { useEffect, useState } from 'react';

import './App.css';

import spellcraftImage1 from './assets/images/spellcraft-logo-1.jpg'
import spellcraftImage2 from './assets/images/spellcraft-logo-2.jpg'

import ELEMENTS from './assets/data/elements.csv.json';
import MODES from './assets/data/modes.csv.json';
import CATEGORIES from './assets/data/categories.csv.json';
import SPELLS from './assets/data/spells.csv.json';


const Clicker = (props) => {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h2>Clicker</h2>
      <span>You clicked {count} times!</span>
      <button style={{ marginLeft: '10px' }} onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}


const ModeDisplay = (props) =>
  <div>
    <h2>Mode</h2>
    <ul>
      {MODES.map(mode => <li key={mode.code}>{mode.code}: {mode.name}</li>)}
    </ul>
  </div>


const ElementDisplay = (props) =>
  <div>
    <h2>Elements</h2>
    <ul>
      {ELEMENTS.map(element => <li key={element.code}>{element.code}: {element.name}</li>)}
    </ul>
  </div>


const CategoryDisplay = (props) =>
  <div>
    <h2>Categories</h2>
    <ul>
      {CATEGORIES.map(category => <li key={category.code}>{category.code}: {category.name}</li>)}
    </ul>
  </div>


const SpellDisplay = (props) =>
  <div>
    <h2>Spell</h2>
    <ul>
      {SPELLS.map(spell => <li key={spell.code}>{spell.code} | {spell.name} | {spell.cost} | {spell.category} </li>)}
    </ul>
  </div>


const ElementFilter = (props) => {

  return (
    <div>
      <h3>Element filter</h3>
      <p>{props.elements.map(element => <span key={element.code} style={{ padding: '4px' }}>{element.code}</span>)}</p>
      <span>enabled: {props.config.enabled}</span>
    </div>
  );
}


const SpellTable = (props) => {

  const [filterName, setFilterName] = useState('');
  const [filterCategory, setFilterCategory] = useState([]);

  useEffect(() => {
    console.log('filterName=', filterName);
    console.log('filterCategory=', filterCategory);

    const filterNameLower = filterName.toLowerCase();

    const applySpellNameFilter = filterNameLower.length > 0;
    const applyCategoryFilter = filterCategory.length > 0;
    const applyFilter = applySpellNameFilter || applyCategoryFilter;
    console.log('applyFilter=', applyFilter);

    const table = document.getElementById("spellTable");
    const tbody = table.getElementsByTagName("tbody")[0];
    const trList = Array.from(tbody.getElementsByTagName("tr"));
    trList.forEach(tr => {
      if (!applyFilter) {
        tr.style.display = "";
        return;
      }

      let spellNameMatch = false;
      if (applySpellNameFilter && tr.dataset.spellname) {
        // TODO: https://en.wikipedia.org/wiki/Levenshtein_distance
        // TODO: Auto suggestions and chips, etc.
        spellNameMatch = tr.dataset.spellname.indexOf(filterNameLower) > -1;
      }

      let categoryMatch = false;
      if (applyCategoryFilter && tr.dataset.category) {
        categoryMatch = filterCategory.includes(tr.dataset.category);
      }

      const visible = (!applySpellNameFilter || (applySpellNameFilter && spellNameMatch)) && (!applyCategoryFilter || (applyCategoryFilter && categoryMatch));
      tr.style.display = visible ? "" : "none";
    });
  }, [filterName, filterCategory]);


  const copyElements = ELEMENTS.map(element => {
    return {
      ...element
    }
  });
  const elementFilterConfig = {
    enabled: false,
    elements: copyElements,
  };

  return (
    <div>
      <h2>Spell table</h2>
      <div>
        <h3>Filter</h3>

        <div>
          <label htmlFor="filterName" style={{ marginRight: '10px' }}>Name</label>
          <input type="text" id="filterName" name="filterName" value={filterName} onChange={event => setFilterName(event.target.value)} placeholder="Examples: Fire, Frost" />
        </div>

        <div>
          <label htmlFor="filterCategory" style={{ marginRight: '10px' }}>Category</label>
          <select id="filterCategory" name="filterCategory" multiple={true} value={filterCategory}
            onChange={event => setFilterCategory(Array.from(event.target.options).filter(x => x.selected).map(x => x.value))}
            >
            {props.categories.map(category => <option key={category.code} value={category.code}>{category.name}</option>)}
          </select>
          <button type='button' onClick={() => setFilterCategory([])}>Clear</button>
        </div>

        <div>
          <ElementFilter config={elementFilterConfig} elements={props.elements} />
        </div>

      </div>
      <table id="spellTable">
        <thead>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Cost</th>
            <th>Category</th>
          </tr>
        </thead>
        <tbody>
          {props.spells.map(spell =>
            <tr key={spell.code} data-spellname={spell.name.toLowerCase()} data-category={spell.category.toLowerCase()}>
              <td>{spell.code}</td>
              <td>{spell.name}</td>
              <td>{spell.cost}</td>
              <td>{spell.category}</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );

}


const App = () => {

  return (
    <div className="App">
      <header className="App-header">
        <h1>Spellcraft</h1>
        <img src={spellcraftImage1} alt="spellcraftImage1" />
        <img src={spellcraftImage2} alt="spellcraftImage2" />
      </header>
      <main>
        <Clicker />
        <ModeDisplay />
        <ElementDisplay />
        <CategoryDisplay />
        {/* <SpellDisplay /> */}
        <SpellTable spells={SPELLS} categories={CATEGORIES} elements={ELEMENTS} />
      </main>
      <footer>
        <p>fuhoi</p>
      </footer>
    </div>
  );
}


export default App;

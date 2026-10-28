import { useEffect } from 'react';
import { SITE_NAME, buildRecipeJsonLd, buildRecipeSeoMeta } from '../utils/seo';

export const useRecipeSeo = (recipe) => {
  useEffect(() => {
    if (!recipe) return undefined;

    const pageUrl = window.location.href;
    const meta = buildRecipeSeoMeta(recipe, pageUrl);
    const jsonLd = buildRecipeJsonLd(recipe, pageUrl);
    if (!meta || !jsonLd) return undefined;

    const previousTitle = document.title;
    const createdNodes = [];
    const previousAttributes = [];

    const setMeta = (attribute, key, content) => {
      if (!content) return;

      let element = document.head.querySelector(`meta[${attribute}="${key}"]`);
      if (element) {
        previousAttributes.push([element, 'content', element.getAttribute('content')]);
      } else {
        element = document.createElement('meta');
        element.setAttribute(attribute, key);
        document.head.appendChild(element);
        createdNodes.push(element);
      }

      element.setAttribute('content', content);
    };

    const setProperty = (property, content) => setMeta('property', property, content);
    const setName = (name, content) => setMeta('name', name, content);

    document.title = meta.title;

    setName('description', meta.description);
    setName('robots', meta.isPublished ? 'index,follow' : 'noindex,follow');

    setProperty('og:type', meta.type);
    setProperty('og:site_name', SITE_NAME);
    setProperty('og:title', meta.title);
    setProperty('og:description', meta.description);
    setProperty('og:url', meta.url);
    setProperty('og:image', meta.image);
    setProperty('og:image:alt', meta.imageAlt);
    setProperty('article:published_time', meta.publishedTime);
    setProperty('article:author', meta.author);

    setName('twitter:card', meta.image ? 'summary_large_image' : 'summary');
    setName('twitter:title', meta.title);
    setName('twitter:description', meta.description);
    setName('twitter:image', meta.image);

    let canonical = document.head.querySelector('link[rel="canonical"]');
    if (canonical) {
      previousAttributes.push([canonical, 'href', canonical.getAttribute('href')]);
    } else {
      canonical = document.createElement('link');
      canonical.setAttribute('rel', 'canonical');
      document.head.appendChild(canonical);
      createdNodes.push(canonical);
    }
    canonical.setAttribute('href', meta.url);

    const jsonLdScript = document.createElement('script');
    jsonLdScript.type = 'application/ld+json';
    jsonLdScript.setAttribute('data-recipe-jsonld', 'true');
    jsonLdScript.textContent = JSON.stringify(jsonLd);
    document.head.appendChild(jsonLdScript);
    createdNodes.push(jsonLdScript);

    return () => {
      document.title = previousTitle;
      createdNodes.forEach((node) => node.remove());
      previousAttributes.forEach(([element, attribute, value]) => {
        if (value === null) {
          element.removeAttribute(attribute);
        } else {
          element.setAttribute(attribute, value);
        }
      });
    };
  }, [recipe]);
};

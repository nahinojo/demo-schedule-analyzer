module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'standard-with-typescript'
  ],
  ignorePatterns: ['src/static/*'],
  overrides: [{
    files: ['*.js'],
    parser: 'espree'
  }],
  parserOptions: {
    ecmaVersion: 'latest',
    project: 'tsconfig.json',
    sourceType: 'module'
  },
  plugins: [
    'react'
  ],
  rules: {
    '@typescript-eslint/indent': 'off',
    '@typescript-eslint/no-unused-vars': 'warn',
    'arrow-body-style': ['error', 'always'],
    'function-call-argument-newline': ['error', 'consistent'],
    'function-paren-newline': ['error', {
      minItems: 2
    }],
    'implicit-arrow-linebreak': ['error', 'below'],
    indent: ['error', 2, {
      ArrayExpression: 'first',
      FunctionExpression: {
        body: 1,
        parameters: 1
      },
      MemberExpression: 1,
      ObjectExpression: 'first'
    }],
    'newline-per-chained-call': ['error', {
      ignoreChainWithDepth: 1
    }],
    'react/boolean-prop-naming': ['error'],
    'react/button-has-type': ['error'],
    'react/destructuring-assignment': ['error', 'always', {
      destructureInSignature: 'always'
    }],
    'react/forbid-component-props': ['error'],
    'react/function-component-definition': ['error', {
      namedComponents: 'arrow-function',
      unnamedComponents: 'arrow-function'
    }],
    'react/hook-use-state': ['error', {
      allowDestructuredState: true
    }],
    'react/jsx-boolean-value': ['error', 'always'],
    'react/jsx-child-element-spacing': ['error'],
    'react/jsx-closing-bracket-location': ['error', 'tag-aligned'],
    'react/jsx-closing-tag-location': ['error', 'tag-aligned'],
    'react/jsx-curly-newline': ['error', {
      multiline: 'require'
    }],
    'react/jsx-curly-spacing': ['error', {
      children: true,
      when: 'never'
    }],
    'react/jsx-equals-spacing': ['error', 'never'],
    'react/jsx-first-prop-new-line': ['error', 'always'],
    'react/jsx-handler-names': ['error'],
    'react/jsx-indent-props': ['error', 2],
    'react/jsx-newline': ['error', {
      prevent: true
    }],
    'react/jsx-no-leaked-render': ['error', {
      validStrategies: ['coerce']
    }],
    'react/jsx-no-useless-fragment': ['error', {
      allowExpressions: true
    }],
    'react/jsx-pascal-case': ['error'],
    'react/jsx-props-no-multi-spaces': ['error'],
    'react/jsx-sort-props': ['error', {
      callbacksLast: true,
      multiline: 'first',
      noSortAlphabetically: false,
      shorthandFirst: true
    }],
    'react/jsx-tag-spacing': ['error', {
      afterOpening: 'never',
      beforeClosing: 'never',
      beforeSelfClosing: 'always',
      closingSlash: 'never'
    }],
    'react/jsx-wrap-multilines': ['error', {
      arrow: 'parens-new-line',
      assignment: 'parens-new-line',
      condition: 'parens-new-line',
      declaration: 'parens-new-line',
      logical: 'parens-new-line',
      prop: 'parens-new-line',
      return: 'parens-new-line'
    }],
    'react/no-access-state-in-setstate': ['error'],
    'react/no-adjacent-inline-elements': ['error'],
    'react/no-danger': ['error'],
    'react/no-multi-comp': ['error'],
    'react/no-object-type-as-default-prop': ['error'],
    'react/no-this-in-sfc': ['error'],
    'react/no-typos': ['error'],
    'react/no-unstable-nested-components': ['error'],
    'react/no-unused-state': ['error'],
    'react/prefer-stateless-function': ['error'],
    'react/self-closing-comp': ['error', {
      component: true,
      html: false
    }],
    'sort-keys': ['error', 'asc', {
      natural: true
    }]
  },
  settings: {
    react: {
      version: 'detect'
    }
  }
}

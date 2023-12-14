import type { StringSelections } from './StringSelections'
import type { TermSelections } from './TermSelections'
import type { YearSelections } from './YearSelections'

export interface CategoriesSelections {
  instructors: StringSelections | null
  courseCode: StringSelections | null
  term: TermSelections | null
  year: YearSelections | null
}
